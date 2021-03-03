from django.urls import path
from . import views
urlpatterns = [
	path('',views.demo),
	path('buy-this/<int:pk>',views.buy_this),
]