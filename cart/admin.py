from django.contrib import admin
from .models import Cart, CartContent
# Register your models here.


class CartAdmin(admin.ModelAdmin):
	list_display = ['user','t_amount']

class CartContentAdmin(admin.ModelAdmin):
	list_display = ['cart','product','qty','amount']
	list_filter = ['cart','product']


admin.site.register(Cart,CartAdmin)
admin.site.register(CartContent,CartContentAdmin)