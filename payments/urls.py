from django.urls import path
from . import views
urlpatterns = [
	path('',views.demo),
	path('payment-page',views.make_payment),
]