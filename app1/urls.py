from django.urls import path
from .views import Rest_list, Rest_detail
from django.conf.urls import url


app_name  = "app1"

urlpatterns=[
	
	url(r'restaurants/$',Rest_list ,name='rest'),
	path('restaurants/<int:id>',Rest_detail,name='Rest_detail')
]
   
   