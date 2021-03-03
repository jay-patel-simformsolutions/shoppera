from django.shortcuts import render, HttpResponse
from products.models import Product
# Create your views here.


def demo(request):
	return HttpResponse('In products')


def buy_this(request,pk):
	product = Product.objects.get(id=pk)
	context  = {}
	context['product'] = product
	return render(request,'products/product.html',context)