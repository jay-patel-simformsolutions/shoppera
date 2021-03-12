from django.db import models

# Create your models here.


class Category(models.Model):
	"""model of category"""
	category_name = models.CharField(max_length=50)
	category_description = models.CharField(max_length=150)

	def __str__(self):
		return self.category_name

	class Meta:
		db_table = 'category'


class Product(models.Model):
	"""model of Products"""
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	product_title = models.CharField(max_length=35)
	product_description = models.CharField(max_length=150)
	product_price = models.IntegerField()
	product_mrp = models.IntegerField()
	product_primary_image = models.ImageField()
	product_color = models.CharField(max_length=150)
	product_trending = models.BooleanField(default=False)

	def __str__(self):
		return self.product_title

	class Meta:
		db_table = 'product'
		

class ProductImages(models.Model):
	"""docstring for ProductImages"""
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	product_secondary_images = models.ImageField()

	def __str__(self):
		return self.product.product_title + '_image'

	class Meta:
		db_table = 'product_images'
		