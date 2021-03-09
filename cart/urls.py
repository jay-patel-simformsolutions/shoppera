from django.urls import path
from . import views
urlpatterns = [
	path('',views.demo),
	path('view-cart/',views.view_cart),
	path('add-product/<int:pk>',views.add_product, name='add_product'),
	path('remove-product/<int:pk>',views.remove_product),
	path('change-quantity',views.change_quantity),
]