from django.contrib import admin
from .models import Category, Product, ProductImages
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_name','category_description']
	search_fields = ('category_name',)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['category','product_title','product_description','product_price','product_mrp','product_primary_image']
	search_fields = ('product_title','product_description')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages)