from django.db import models
from administration.models import User
from products.models import Product
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Create your models here.

class Cart(models.Model):
	"""model for cart"""
	user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
	t_amount = models.IntegerField()

	def __str__(self):
		return str(self.user) + ' Cart'

	class Meta:
		db_table = 'cart'


class CartContent(models.Model):
	"""model for cart content"""

	cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	qty = models.IntegerField()
	amount = models.IntegerField()

	def __str__(self):
		return str(self.cart.user) + ' CartContent'

	class Meta:
		db_table = 'cart_content'
		unique_together = ['cart', 'product']


@receiver(post_save, sender=CartContent)
def change_tamount(sender,**kwargs):
	print('Hello From signals')
	cart = Cart.objects.get(id = kwargs['instance'].cart_id)
	cart_content = CartContent.objects.filter(cart = cart)
	t_amount = 0
	for i in cart_content:
		t_amount += i.amount

	cart.t_amount = t_amount
	cart.save()
	return 'done'

@receiver(post_delete, sender=CartContent)
def change_tamount1(sender,**kwargs):
	print('Hello From signals')
	cart = Cart.objects.get(id = kwargs['instance'].cart_id)
	cart_content = CartContent.objects.filter(cart = cart)
	t_amount = 0
	for i in cart_content:
		t_amount += i.amount

	cart.t_amount = t_amount
	cart.save()
	return 'done'