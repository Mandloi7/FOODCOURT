from django.db import models
from django.contrib.auth.models import AbstractUser
from app1.models import foodpair
# Create your models here.

class CustomUser(AbstractUser):
    ucart = models.ForeignKey('cart', on_delete=models.CASCADE, null=True)


class cart(models.Model):
	foodp = models.ManyToManyField('app1.foodpair')

