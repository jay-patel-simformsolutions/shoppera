from django.shortcuts import render, HttpResponse
from .serializers import ProductSerializer
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

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


@api_view(['GET'])
def filter_products(request):
	price_from = request.GET['price_from']
	price_to = request.GET['price_to']
	color = request.GET['color']
	products = request.session['products']
	data = []
	for product in products:
		if product['product_price'] >= int(price_from) and product['product_price'] <= int(price_to) and product['product_color'] == color:
			data.append(product)
	html_products = render(request,'products/search_products_section.html',{'products' : data})
	return render(request,'products/search_products_section.html', {'products' : data})


class ProductPractice(RetrieveAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()
