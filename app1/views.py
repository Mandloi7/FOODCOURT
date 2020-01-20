from django.shortcuts import render,get_object_or_404
from .models import restaurant
from app1.models import food
# Create your views here.


def Rest_list(request):
	restaurants = restaurant.objects.all()
	return render(request, 'registration/rest_list.html', {'restaurants' : restaurants})



def Rest_detail(request,id):

	Restaurant = get_object_or_404(restaurant,pk=id)
	x=Restaurant.food_set.all()
	print(x)
	return render(request, 'registration/rest_detail.html', {'Restaurant' : Restaurant})