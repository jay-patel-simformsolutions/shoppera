from django.urls import path
from . import views
urlpatterns = [
	path('',views.demo),
	path('buy-this/<int:pk>',views.buy_this, name='buy_this'),
	path('product-data/<int:pk>',views.product_data, name='product_data'),
	path('filter-products',views.filter_products, name='filter_products'),
]