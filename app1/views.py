from django.shortcuts import render,get_object_or_404,redirect
from .models import restaurant
from app1.models import food,order,foodpair
from users.models import cart,CustomUser
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from PAYTM import checksum
from django.http import HttpResponse
from decimal import *
# Create your views here.
MERCHANT_ID="IOqCTP42042072367821"
MERCHANT_KEY=r"dE@%WPxdSm3Scs2@"
TWOPLACES = Decimal(10) ** -2 

@login_required(login_url='home')
def Rest_list(request):
	restaurants = restaurant.objects.all()
	return render(request, 'registration/rest_list.html', {'restaurants' : restaurants})

@login_required(login_url='home')
def Rest_detail(request,id):

	Restaurant = get_object_or_404(restaurant,pk=id)
	x=Restaurant.food_set.all()
	# print(x)
	con={
	'Restaurant' : Restaurant,
	'cart':cart,
	}
	return render(request, 'registration/rest_detail.html', con)


@login_required(login_url='home')
def pay(request):
	myorder=order.objects.latest('pk')
	total=myorder.total
	tot=Decimal(total).quantize(TWOPLACES)
	totstr=str(tot)
	data_dic={'MID':MERCHANT_ID,
            'ORDER_ID':str(myorder.id),
            'TXN_AMOUNT':totstr,
            'CUST_ID':str(request.user.email),
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
	    	'CALLBACK_URL':'http://127.0.0.1:8000/app1/paytm/',
	    }
	data_dic["CHECKSUMHASH"]=checksum.generate_checksum(data_dic,MERCHANT_KEY)
	return render(request,'registration/payview.html',{'data_dic':data_dic})


def makeOrder(request):
	tot='0'
	qtydic={}
	if request.method =="POST":
		tot=request.POST.get('total','0')
		qtydic=json.loads(request.POST.get('qtydic',None))
		print("------------")
		print(tot)
		print(qtydic)
	
	myorder = order.objects.create(name=str(request.user.email),total=int(tot))
	myorder.save()
	print(myorder)

	for foodname,val in qtydic.items(): 
		foodval=food.objects.filter(fname=foodname)
		newfood=foodpair.objects.create(food=foodval[0],qty=int(val),ordername=myorder)
		newfood.save()
	print("DONE")
	return render(request,'registration/makeorder.html',{})

@login_required(login_url='home')
def confirmOrder(request):
	print("up")
	myorder = order.objects.latest('pk')
	print('down')
	# tot=myorder.total
	foodp=myorder.foodpair_set.all()
	print(foodp)
	return render(request,'registration/confirmOrder.html',{'foodp':foodp})

@login_required(login_url='home')
@csrf_exempt
def paytm(request):
	return HttpResponse("Payment-Done")