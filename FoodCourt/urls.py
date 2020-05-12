"""FoodCourt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users.views import HomeView
from app1.views import Rest_list
from . import settings
from django.conf.urls.static import static
from app1.views import pay
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.url')),
    path('users/',include('django.contrib.auth.urls')),
    path('',HomeView,name='home'),
    path('app1/', include('app1.urls', namespace="app1")),
    path('payment/',pay,name="pay")
    # path('restaurants/',Rest_list ,name='rest'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)