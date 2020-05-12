from django.db import models
from phone_field import PhoneField
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class restaurant(models.Model):
	rname = models.CharField(max_length=250)
	rphone = PhoneNumberField(null=False, blank=False, unique=True)
	rrating = models.DecimalField(max_digits=5,decimal_places=1)
	cuisine = models.TextField(default="")
	rimg = models.ImageField(upload_to='restaurant/')

	def __str__ (self):
			return self.rname


class food(models.Model):
	fname = models.CharField(max_length=250)
	fmoney = models.PositiveIntegerField(default=0)
	fimg = models.ImageField(upload_to='food/',blank=True,null=True)
	frating = models.DecimalField(max_digits=5,decimal_places=1)
	fcat = models.ForeignKey('fcat', on_delete=models.CASCADE, null=True)
	frestaurant = models.ForeignKey('restaurant', on_delete=models.CASCADE, null=True)

	def __str__ (self):
			return self.fname


class foodpair(models.Model):
	food = models.ForeignKey('food',on_delete=models.CASCADE,null=True)
	qty = models.PositiveIntegerField(default=0,null=True)
	ordername=models.ForeignKey('order',on_delete=models.CASCADE,null=True)

class fcat(models.Model):
	cname = models.CharField(max_length=250)
	def __str__ (self):
			return self.cname

class order(models.Model):
	name=models.EmailField(max_length=254,null=True)
	total=models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.name
