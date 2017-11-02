import re
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from .models import Queryer
from django.forms import ModelForm

class RegistrationForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'id':'reg','placeholder':'Username'}))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'id':'reg','placeholder':'Email'}))
    firstname = forms.CharField(label='',widget=forms.TextInput(attrs={'id':'reg','placeholder':'Firstname'}))
    password1 = forms.CharField(label='',
                          widget=forms.PasswordInput(attrs={'id':'reg','placeholder': 'Password'}))
    password2 = forms.CharField(label='',
                        widget=forms.PasswordInput(attrs={'id':'reg','placeholder': 'Repeat Password'}))
    def clean_password2(self):
    	if 'password1' in self.cleaned_data:
    		password1 = self.cleaned_data['password1']
    		password2 = self.cleaned_data['password2']
    		if password1 == password2:
    			return password2
    	raise forms.ValidationError('Passwords do not match.')
    def clean_username(self):
    	username = self.cleaned_data['username']
    	if not re.search(r'^\w+$',username):
    		raise forms.Validation('Username can only contain alphanumeric characters')
    	try:
    		User.objects.get(username=username)
    	except ObjectDoesNotExist:
    		return username
    	raise forms.ValidationError('Username is already taken.')

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))



class inputForm(ModelForm):
    name                 = models.CharField(max_length=200)
    code                 = models.CharField(max_length=15)
    international        = models.BooleanField()
    pathways             = models.BooleanField()
    scholarship          = models.BooleanField()
    advancedstanding     = models.BooleanField()
    year12               = models.BooleanField()
    def __init__(self, *args, **kwargs):
         super(inputForm, self).__init__(*args, **kwargs)
         self.fields['name'].label = ''
         self.fields['code'].label = ''
         # self.fields['international'].label = ''
         # self.fields['pathways'].label = ''
         # self.fields['scholarship'].label = ''
         # self.fields['advancedstanding'].label = ''
         # self.fields['year12'].label = ''
    class Meta:
        model = Queryer
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Students Name'}),
            'code': forms.TextInput(attrs={'placeholder':'Course Code'}),
            # 'international':forms.CheckboxInput(attrs={'checked':'unchecked'}),
            # 'pathways':forms.CheckboxInput(attrs={'checked':'unchecked'}),
            # 'scholarship':forms.CheckboxInput(attrs={'checked':'unchecked'}),
            # 'advancedstanding':forms.CheckboxInput(attrs={'checked':'unchecked'}),
            # 'year12':forms.CheckboxInput(attrs={'checked':''}),

        }
        fields = ['name','code','international','pathways','scholarship','advancedstanding','year12']







