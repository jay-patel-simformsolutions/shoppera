from django.db import models
from orders.models import Order
# Create your models here.

class Payment(models.Model):
	"""model for Payments"""
	order = models.ForeignKey(Order,on_delete=models.CASCADE)
	date_of_payment = models.DateField()
	mode_of_payment = models.CharField(max_length=50)
	transaction_id = models.BigIntegerField()

	def __str__(self):
		return str(self.order) + ' Payment'

	class Meta:
		db_table = 'payment'