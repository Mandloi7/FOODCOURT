from django.urls import path
from . import views 
from django.conf.urls import url

app_name  = "app1"

urlpatterns=[
	
	url(r'restaurants/$',views.Rest_list ,name='rest'),
	path('restaurants/<int:id>',views.Rest_detail,name='Rest_detail'),
	path('paytm/',views.paytm,name='paytm'),
	path('pay/',views.pay,name='pay'),
	path('confirmOrder/',views.confirmOrder,name='confirmorder'),
	path('makeorder/',views.makeOrder,name="makeorder")
]
   
   