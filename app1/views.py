from django.shortcuts import render
from .models import restaurant
# Create your views here.


def Rest_list(request):
	restaurants = restaurant.objects.all()
	return render(request, 'registration/rest_list.html', {'restaurants' : restaurants})



def Rest_detail(request, restaurant_pk):
	foods = restaurant.objects.filter( restaurant_pk=restaurant_pk )
	return render(request, 'registration/rest_detail.html', {'restaurant' : foods})