from django.shortcuts import render, HttpResponse
from .serializers import ProductSerializer
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


def demo(request):
	return HttpResponse('In products')


def buy_this(request,pk):
	product = Product.objects.get(id=pk)
	context  = {}
	context['product'] = product
	return render(request,'products/product.html',context)


@api_view(['GET'])
def product_data(request, pk):
	product = Product.objects.get(id=pk)
	serializer = ProductSerializer(product)
	return Response(serializer.data)