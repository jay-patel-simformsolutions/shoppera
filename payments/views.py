from django.shortcuts import render, HttpResponse

# Create your views here.


def demo(request):
	return HttpResponse('In payments')


def make_payment(request):
	return render(request,'payments/make-payment.html')