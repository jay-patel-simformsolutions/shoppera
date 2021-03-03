from django.db import models
from administration.models import User
from products.models import Product
# Create your models here.


class Order(models.Model):
	"""model for orders"""
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	delivery_address = models.CharField(max_length=300)
	total_amount = models.IntegerField()
	date_of_order = models.DateField()

	def __str__(self):
		return (self.user) + ' Order'

	class Meta:
		db_table = 'order'


class OrderDetails(models.Model):
	"""model for OrderDetails"""
	order = models.ForeignKey(Order,on_delete=models.CASCADE)
	product = models.ForeignKey(Product,models.CASCADE)
	qty = models.IntegerField()
	amount = models.IntegerField()

	def __str__(self):
		return (self.order) + ' OrderDetails'

	class Meta:
		db_table = 'order_details'
		