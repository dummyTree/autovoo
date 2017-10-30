
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here
#form writes to query
class Queryer(models.Model):
	user                 = models.ForeignKey(User,)
	uuidqueryer          = models.CharField(max_length=25)
	name                 = models.CharField(max_length=200)
	code                 = models.CharField(max_length=15)
	international        = models.BooleanField()
	pathways             = models.BooleanField()
	scholarship          = models.BooleanField()
	advancedstanding     = models.BooleanField()
	year12               = models.BooleanField()

	def __str__(self):
		return self.name

#view loads query to generate string then saves to below for
#data which can be used as training data on Neural Network or 
#display recent searches

class Output(models.Model):
	name = models.ForeignKey(Queryer, on_delete=models.CASCADE)
	advancedstanding = models.CharField(max_length=200)
	def __str__(self):
		return self


