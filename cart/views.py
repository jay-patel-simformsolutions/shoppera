from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from cart.models import Cart, CartContent
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.


def demo(request):
	return HttpResponse('In cart')

@login_required
def view_cart(request):
	cart = Cart.objects.get(user_id=request.user)
	cart_content = CartContent.objects.filter(cart=cart)
	context = {}
	context['cart_content'] = cart_content
	context['total_amount'] = cart.t_amount
	return render(request,'cart/cart.html',context)


@login_required
def add_product(request,pk):
	product = Product.objects.get(id=pk)
	cart = Cart.objects.get(user_id=request.user)
	cart_content = CartContent()
	cart_content.cart = cart
	cart_content.product = product
	cart_content.qty = 1
	cart_content.amount = product.product_price
	try:
		cart_content.save()
	except IntegrityError:
		cart_content = CartContent.objects.get(cart=cart,product=product)
		cart_content.qty += 1
		cart_content.amount = cart_content.qty * product.product_price
		cart_content.save()
	finally:
		cart.t_amount += cart_content.amount
		cart.save()
	return redirect('/cart/view-cart')


@login_required
def remove_product(request,pk):
	cart = Cart.objects.get(user = request.user)
	product = Product.objects.get(id=pk)
	cart_product = CartContent.objects.get(cart=cart,product=product).delete()
	return redirect('/cart/view-cart')

@csrf_exempt
def change_quantity(request):
	data = json.loads(request.body.decode('UTF-8'))
	cart_content = CartContent.objects.get(id=data['id'])
	cart_content.qty = data['qty']
	cart_content.amount = cart_content.qty * cart_content.product.product_price
	cart_content.save()
	response = {}
	response['t_amount'] = cart_content.cart.t_amount
	return HttpResponse(json.dumps(response), content_type="application/json")