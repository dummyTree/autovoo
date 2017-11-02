from django import forms
from django.db import models
from .models import Scripts
from django.forms import ModelForm

class EmailScripts(ModelForm):
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
	# def __init__(self, *args, **kwargs):
	#      super(EmailScripts, self).__init__(*args, **kwargs)
	#      self.fields['HiScript'].label = ''
	#      self.fields['ThanksScript'].label = ''
	#      # self.fields['ApplicationDateMature'].label = ''
	#      # self.fields['ApplicationDateYear12'].label = ''
	#      # self.fields['ApplicationDateGeneric'].label = ''
	#      # self.fields['AcceptingApplicationsNo'].label = ''
	#      # self.fields['AcceptingApplicationsPG'].label = ''
	#      # self.fields['AcceptingApplicationsINT'].label = ''
	#      # self.fields['AdmissionInfo'].label = ''
	#      # self.fields['PathwaysInfo'].label = ''
	#      # self.fields['ScholarshipInfo'].label = ''
	class Meta:
		model = Scripts
		widgets = {
		'HiScript': forms.TextInput(attrs={'type':'hidden','class':'hiddeninput'}),
		'ThanksScript': forms.TextInput(attrs={'type':'hidden','class':'hiddeninput'}),
		'ApplicationDateMature': forms.TextInput(attrs={'type':'hidden','class':'hiddeninput'}),
		'ApplicationDateYear12':forms.TextInput(attrs={'type':'hidden','class':'hiddeninput'}),
		'ApplicationDateGeneric':forms.TextInput(attrs={'type':'hidden','class':'hiddeninput'}),
		'AcceptingApplicationsNo':forms.TextInput(attrs={'type':'hidden','class':'hiddeninput'}),
		'AcceptingApplicationsPG':forms.TextInput(attrs={'type':'hidden','class':'hiddeninput'}),
		'AcceptingApplicationsINT':forms.TextInput(attrs={'type':'hidden','class':'hiddeninput'}),
		'AdmissionInfo': forms.TextInput(attrs={'type':'hidden','class':'hiddeninput'}),
		'PathwaysInfo':forms.TextInput(attrs={'type':'hidden','class':'hiddeninput'}),
		'ScholarshipInfo':forms.TextInput(attrs={'type':'hidden','class':'hiddeninput'}),
		'AdvancedStandingInfo':forms.TextInput(attrs={'type':'hidden','class':'hiddeninput'}),
		'close_off_DOM':forms.TextInput(attrs={'type':'hidden','class':'hiddeninput'}),
		'close_off_INT':forms.TextInput(attrs={'type':'hidden','class':'hiddeninput'}),

		}
		fields = [ 'HiScript','ThanksScript','ApplicationDateMature','ApplicationDateYear12','ApplicationDateGeneric','AcceptingApplicationsNo','AcceptingApplicationsPG','AcceptingApplicationsINT','AdmissionInfo','PathwaysInfo','ScholarshipInfo','AdvancedStandingInfo','close_off_DOM','close_off_INT']




