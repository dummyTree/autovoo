from django.shortcuts import render
from django.http import HttpResponse 
from .models import Scripts
from .forms import *
from django.contrib.auth.models import User
# Create your views here.

def regemail(request):
	checkuser = request.user.username
	scripts = Scripts.objects.filter(user=request.user).values('user_id')
	#if yes: display these values in form
	if scripts:
		if request.method == 'POST':
			form = EmailScripts(request.POST)
			# ThanksScript=
			scripts = Scripts.objects.filter(user=request.user).first()
			HiScript=request.POST['HiScript']
			ThanksScript =request.POST['ThanksScript']
			ApplicationDateMature = request.POST['ApplicationDateMature']
			ApplicationDateYear12 =request.POST['ApplicationDateYear12']
			ApplicationDateGeneric = request.POST['ApplicationDateGeneric']
			AcceptingApplicationsNo =request.POST['AcceptingApplicationsNo']
			AcceptingApplicationsPG = request.POST['AcceptingApplicationsPG']
			AcceptingApplicationsINT =request.POST['AcceptingApplicationsINT']
			AdmissionInfo = request.POST['AdmissionInfo']
			PathwaysInfo =request.POST['PathwaysInfo']
			ScholarshipInfo = request.POST['ScholarshipInfo']
			AdvancedStandingInfo = request.POST['AdvancedStandingInfo']
			close_off_DOM =request.POST['close_off_DOM']
			close_off_INT = request.POST['close_off_INT']
			scripts.HiScript = HiScript
			scripts.ThanksScript =ThanksScript
			scripts.ApplicationDateMature = ApplicationDateMature
			scripts.ApplicationDateYear12 = ApplicationDateYear12
			scripts.ApplicationDateGeneric = ApplicationDateGeneric
			scripts.AcceptingApplicationsNo = AcceptingApplicationsNo
			scripts.AcceptingApplicationsPG = AcceptingApplicationsPG
			scripts.AcceptingApplicationsINT = AcceptingApplicationsINT
			scripts.AdmissionInfo = AdmissionInfo
			scripts.PathwaysInfo = PathwaysInfo
			scripts.ScholarshipInfo = ScholarshipInfo
			scripts.AdvancedStandingInfo = AdvancedStandingInfo
			scripts.close_off_DOM = close_off_DOM
			scripts.close_off_INT = close_off_INT

			scripts.save()
		else:
			
			scripts = Scripts.objects.filter(user=request.user).values( 'HiScript','ThanksScript','ApplicationDateMature','ApplicationDateYear12','ApplicationDateGeneric','AcceptingApplicationsNo','AcceptingApplicationsPG','AcceptingApplicationsINT','AdmissionInfo','PathwaysInfo','ScholarshipInfo','AdvancedStandingInfo','close_off_DOM','close_off_INT').first()
			data = {'HiScript':scripts['HiScript'],'ThanksScript':scripts['ThanksScript'],'ApplicationDateMature':scripts['ApplicationDateMature'],'ApplicationDateYear12':scripts['ApplicationDateYear12'],'ApplicationDateGeneric':scripts['ApplicationDateGeneric'],'AcceptingApplicationsNo':scripts['AcceptingApplicationsNo'],'AcceptingApplicationsPG':scripts['AcceptingApplicationsPG'],'AcceptingApplicationsINT':scripts['AcceptingApplicationsINT'],'AdmissionInfo':scripts['AdmissionInfo'],'PathwaysInfo':scripts['PathwaysInfo'],'ScholarshipInfo':scripts['ScholarshipInfo'],'AdvancedStandingInfo':scripts['AdvancedStandingInfo'],'close_off_DOM':scripts['close_off_DOM'],'close_off_INT':scripts['close_off_INT']}
			form = EmailScripts(initial=data)		
	
		return render(
			request,
			'registration/profile.html',
			{'form':form},
			)


	#if no: desplay default from user Generic
	else:
		print('user does not exist')
		if request.method == 'POST':
			form = EmailScripts(request.POST)
			HiScript=request.POST['HiScript']
			ThanksScript =request.POST['ThanksScript']
			ApplicationDateMature = request.POST['ApplicationDateMature']
			ApplicationDateYear12 =request.POST['ApplicationDateYear12']
			ApplicationDateGeneric = request.POST['ApplicationDateGeneric']
			AcceptingApplicationsNo =request.POST['AcceptingApplicationsNo']
			AcceptingApplicationsPG = request.POST['AcceptingApplicationsPG']
			AcceptingApplicationsINT =request.POST['AcceptingApplicationsINT']
			AdmissionInfo = request.POST['AdmissionInfo']
			PathwaysInfo =request.POST['PathwaysInfo']
			ScholarshipInfo = request.POST['ScholarshipInfo']
			AdvancedStandingInfo = request.POST['AdvancedStandingInfo']
			close_off_DOM =request.POST['close_off_DOM']
			close_off_INT = request.POST['close_off_INT']
			newscripts = Scripts.objects.create(user=request.user, HiScript=HiScript, ThanksScript=ThanksScript,ApplicationDateMature=ApplicationDateMature,ApplicationDateYear12=ApplicationDateYear12,ApplicationDateGeneric=ApplicationDateGeneric,AcceptingApplicationsNo=AcceptingApplicationsNo,AcceptingApplicationsPG=AcceptingApplicationsPG,AcceptingApplicationsINT=AcceptingApplicationsINT,AdmissionInfo=AdmissionInfo,PathwaysInfo=PathwaysInfo,ScholarshipInfo=ScholarshipInfo,AdvancedStandingInfo=AdvancedStandingInfo,close_off_INT=close_off_INT,close_off_DOM=close_off_DOM)
			
		else:
			generic = User.objects.filter(username='generic').first()
			scripts = Scripts.objects.filter(user=generic).values( 'HiScript','ThanksScript','ApplicationDateMature','ApplicationDateYear12','ApplicationDateGeneric','AcceptingApplicationsNo','AcceptingApplicationsPG','AcceptingApplicationsINT','AdmissionInfo','PathwaysInfo','ScholarshipInfo','AdvancedStandingInfo','close_off_DOM','close_off_INT').first()
			HiScript=scripts['HiScript']
			data = {'HiScript':scripts['HiScript'],'ThanksScript':scripts['ThanksScript'],'ApplicationDateMature':scripts['ApplicationDateMature'],'ApplicationDateYear12':scripts['ApplicationDateYear12'],'ApplicationDateGeneric':scripts['ApplicationDateGeneric'],'AcceptingApplicationsNo':scripts['AcceptingApplicationsNo'],'AcceptingApplicationsPG':scripts['AcceptingApplicationsPG'],'AcceptingApplicationsINT':scripts['AcceptingApplicationsINT'],'AdmissionInfo':scripts['AdmissionInfo'],'PathwaysInfo':scripts['PathwaysInfo'],'ScholarshipInfo':scripts['ScholarshipInfo'],'AdvancedStandingInfo':scripts['AdvancedStandingInfo'],'close_off_DOM':scripts['close_off_DOM'],'close_off_INT':scripts['close_off_INT']}
			form = EmailScripts(initial=data)


		return render(
			request,
			'registration/profile.html',
			{'form':form},
			)

