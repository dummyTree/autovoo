from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
# Create your models here.


class Scripts(models.Model):
	user					= models.ForeignKey('auth.User')
	HiScript     			= models.TextField(max_length=1000)
	ThanksScript 			= models.TextField(max_length=1000)
	ApplicationDateMature 	= models.TextField(max_length=1000)
	ApplicationDateYear12	= models.TextField(max_length=1000) 
	ApplicationDateGeneric	= models.TextField(max_length=1000)
	AcceptingApplicationsNo		= models.TextField(max_length=1000)
	AcceptingApplicationsPG		= models.TextField(max_length=1000)
	AcceptingApplicationsINT	= models.TextField(max_length=1000)
	AdmissionInfo			= models.TextField(max_length=1000)
	PathwaysInfo			= models.TextField(max_length=1000)
	ScholarshipInfo			= models.TextField(max_length=1000)
	AdvancedStandingInfo 	= models.TextField(max_length=1000)
	close_off_DOM	= models.TextField(max_length=1000)
	close_off_INT	= models.TextField(max_length=1000)
	def __str__(self):
		return self.user.username