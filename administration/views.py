from django.shortcuts import render, HttpResponse, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product, Category
from django.contrib.auth import authenticate,login,logout
from .forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from administration.models import UserProfile
from cart.models import Cart
from django.db.models import Q
from .serializers import ProductSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.filters import SearchFilter
import django_filters

# from django.db.models import model_to_dict
# Create your views here.


def demo(request):
	categories = Category.objects.all()
	products = Product.objects.all()[:3]
	context = {}
	context['categories'] = categories
	context['products'] = products
	return render(request,'index.html',context)


def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				return redirect('/')
			else:
				return HttpResponse('__________')
		else:
			return HttpResponse('Invalid Login Credentials')
	else:
		return render(request,'login.html')


def register_user(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		user_profile_form = UserProfileForm(request.POST)
		if user_form.is_valid() and user_profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = user_profile_form.save(commit=False)
			profile.user = user
			profile.save()

			cart = Cart()
			cart.user = user
			cart.t_amount = 0
			cart.save()

			return redirect('/login')
		else:
			print(user_form.errors,user_profile_form.errors)
			return HttpResponse('Forms Not Valid')
	else:
		user_form = UserForm()
		user_profile_form = UserProfileForm()
		context = {
			'user_form':user_form,
			'user_profile_form':user_profile_form
		}
		return render(request,'register.html',context)


@login_required
def logout_user(request):
	logout(request)
	return redirect ('/')


@login_required
def user_profile(request,pk):
	user = User.objects.get(id=pk)
	user_profile = UserProfile.objects.get(user=user)
	if request.method == 'GET':
		context = {}
		context['user_obj'] = user
		context['user_form'] = UserForm(instance=user)
		context['user_profile'] = UserProfileForm(instance=user_profile)
		return render(request,'user_profile.html',context)
	else:
		user_form = UserForm(request.POST,instance=user)
		user_profile_form = UserProfileForm(request.POST,instance=user_profile)
		if user_form.is_valid() and user_profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = user_profile_form.save(commit=False)
			profile.user = user
			profile.save()
			return redirect('/login')
		else:
			print(user_form.errors,user_profile_form.errors)
			return HttpResponse('Forms Not Valid')


def search_product(request):
	search_query = request.GET['search']
	products = Product.objects.filter(Q(product_title__contains=search_query) | Q(product_description__contains=search_query))
	context = {}
	context['search_query'] = search_query
	context['products'] = products
	request.session['products'] = list(products.values())
	x = lambda x : x[0]
	colors = list(map(str,map(x,products.values_list('product_color').distinct())))
	# print(list(colors))
	context['colors'] = list(colors)
	return render(request,'admin/product_result_page.html',context)


@api_view(['GET'])
def api_test(request):
	search_query = request.GET['search']
	products = Product.objects.filter(Q(product_title__contains=search_query) | Q(product_description__contains=search_query))
	serializer = ProductSerializer(products,many=True)
	return Response(serializer.data)


class CustomPagination(PageNumberPagination):
	# default_limit = 5
	# max_limit = 2
	page_size = 3


class ProductsApi(ListAPIView):
	serializer_class = ProductSerializer
	# queryset = Product.objects.all()
	pagination_class = CustomPagination
	filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
	search_fields = ['product_title','product_description']
	filterset_fields = ['product_color','product_price']

	def get_queryset(self):
		return Product.objects.all()