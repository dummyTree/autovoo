#import dependencies for Django
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Queryer,Output
from django.contrib.auth.models import User
from .forms import *
from registeremail.models import Scripts
import uuid


#dependencies for scanning
import ssl
from bs4 import BeautifulSoup
import urllib.request

def index(request):
	checkuser = request.user.username
	scripts = Scripts.objects.filter(user=request.user).values('user_id')
	#if yes: display these values in form
	if scripts:
		queryuuid=uuid.uuid4()
		queryuuid=str(queryuuid)[:24]
		my_Query = Queryer.objects.first()
		#this begins form input request
		form = inputForm(instance=my_Query,auto_id=False)
		if request.method == 'POST':
			form = inputForm(request.POST)
			presaved = form.save(commit=False)
			presaved.user = request.user
			presaved.uuidqueryer = queryuuid
			presaved.save()
			form = inputForm()
		#this begins query code that scans website based on form
		
		checkuser = request.user
		print(checkuser)
		search =Queryer.objects.filter(uuidqueryer=queryuuid).values('name','code','advancedstanding','international','pathways','scholarship','year12').first()
		if search:
			print('hello')
			name = search['name']
			print(name)
			course_Code = search['code']
			print(course_Code)
			advanced_Standing = search['advancedstanding']
			international = search['international']
			pathways = search['pathways']
			scholarship = search['scholarship']
			print(scholarship)
			year_12 =  search['year12']
			index_html = "https://www.vu.edu.au"
			

			if(international == False):
				search_Page = "https://www.vu.edu.au/courses/search?type=Course&query="
				search_Page2 = "&iam=resident&op=Search" 
			else:
				search_Page = "https://www.vu.edu.au/courses/search?type=Course&query="
				search_Page2 = "&iam=non-resident&op=Search"
				vuicontact = "<br/><br/>Web: <a href='http://www.vu.edu.au/international/'>http://www.vu.edu.au/international/</a><br/>Email: international@vu.edu.au<br/>Phone: +61 3 9919 1164<br/><br/>If for some reason you have any other questions please let me know by responding to this email! <br/><br/>Kind regards,<br/>Dimitri <br/>Student Service Officer, VUHQ<br/>Phone +61 3 9919 6100 <br/>For additional information, please visit <a href='https://askvu.vu.edu.au/'>ASKVU</a>"
				
			print(search_Page+course_Code+search_Page2)

			#gcontext=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
			ssl._create_default_https_context = ssl._create_unverified_context
			sauce = urllib.request.urlopen(search_Page+course_Code+search_Page2).read()
			soup = BeautifulSoup(sauce,'lxml')
			results = soup.find("ol", class_="results-list")

			if results is not None:
				for url in results.find_all('a'):
					course = url.get('href')
					print(course)
					if(course_Code.lower() in course.lower()):
						print(course_Code.lower())
						print(course.lower())
						course_html = course
						course_Link = index_html+course_html
			
			else:
				if international:
					name_String = "International students are not being accepted for that course. Please check our website for more options."

				else:
					name_String = "Error Course not found"

				return render(
					request,
					'index2.html',
					{'form':form,'name_String':name_String},
					)



			sauce = urllib.request.urlopen(course_Link)

			soup = BeautifulSoup(sauce,'lxml')
			course_Title = soup.find('h1').text

			applications = soup.find('div', id="how-to-apply")
			script = Scripts.objects.filter(user=request.user).values('close_off_DOM').first()
			signoff = "<br/><br/>Kind regards,<br/>{}<br/>Student Service Officer, VUHQ<br/>Phone +61 3 9919 6100 <br/>For additional information, please visit <a href='https://askvu.vu.edu.au/'>ASKVU</a>".format(request.user.get_short_name())

			close_off = script['close_off_DOM'].replace('/-email-sign-off-/',signoff)
			close_off = close_off.replace('/-course-title-/',course_Title)
			close_off = close_off.replace('/-first-name-/',name)

			###################################ADDITIONAL INFORMATION###################################

			additional_Info=""
			if(course_Title=="Graduate Diploma in Migration Law"):
				additional_Info="The course fees for this course will be approximately $22,000 for the whole course, however this will be confirmed in December when the course units are finalised.  The course itself goes for 12 months and is available online and on campus, you can choose an option that is best for yourself. The start date should be early Feb and will end in November, however dates for next year are still tentative."
			if(course_Title=="Master of Education"):
				if(international==True):
					alt_Link = 'https://www.vu.edu.au/courses/international/EMES'
				else:
					alt_Link = 'https://www.vu.edu.au/courses/master-of-teaching-secondary-education-emes'
				additional_Info="You have enquired into the <a href='{}'>Graduate Diploma in Education</a>, this course does not allow someone to become a teacher and is more aimed at allowing people to pursue a research field in education. If you would like to do this information can be found in the link above. However, more likely than not you are hoping to become a teacher, therefore I have placed details below on the <a href='{}'></a>Master of Teaching (Secondary Education)</a>. ".format(course_Link,alt_Link)
			

			###################################Applications Accepted?###################################

			if(international==False):
				if("not being taken at this time" in applications.text):
					script = Scripts.objects.filter(user=request.user).values('AcceptingApplicationsNo').first()
					accepted_Info = script['AcceptingApplicationsNo']
				else:
					bold = applications.find_all('b')
					bold_Size = len(bold)
					if(bold_Size<2):
						script = Scripts.objects.filter(user=request.user).values('AcceptingApplicationsPG').first()
						onlinedate = "<b>{}</b>".format(bold[0].text)
						accepted_Info = script['AcceptingApplicationsPG'].replace('/-online-close-date-/',onlinedate)
					elif(year_12==True):
						script = Scripts.objects.filter(user=request.user).values('ApplicationDateYear12').first()
						vtacdate = "<b>{}</b>".format(bold[0].text)
						accepted_Info = script['ApplicationDateYear12'].replace('/-VTAC-close-date-/',vtacdate)
					else:
						script = Scripts.objects.filter(user=request.user).values('ApplicationDateMature').first()
						onlinedate = "<b>{}</b>".format(bold[1].text)
						accepted_Info = script['ApplicationDateMature'].replace('/-online-close-date-/',onlinedate)
			else:
				script = Scripts.objects.filter(user=request.user).values('AcceptingApplicationsINT','close_off_INT').first()
				applyLinks ="<br><br><a href='http://eaams.vu.edu.au/'>Direct Online Application</a><br><br><a href='http://eaams.vu.edu.au/BrowseAgents.aspx'>Find An Education Agent</a>"
				accepted_Info = script['AcceptingApplicationsINT']
				accepted_Info = accepted_Info.replace('/-apply-links-international-/',applyLinks)

				close_off = script['close_off_INT'].replace('/-first-name-/',name)
				close_off = close_off.replace('/-course-title-/',course_Title)
				close_off = close_off.replace('/-vui-contact-details-/',vuicontact)
			

			################################### REQUIREMENTS ###################################

			admit = soup.find('section', id="admission-information")
			admission_Info = "In order to apply for this course you will need to satisfy the following entry requirements.\n{}".format(admit.text)
			

			################################### Pathways ###################################

			pathway_Info =""
			if(pathways==True):
				pathway_Soup = soup.find('div', class_="pathway")
				if pathway_Soup:
					pathway_Course = pathway_Soup.text
					pathway_Amount = len(pathway_Soup)
					
					pathway= "It is ok if you do not meet those requirements, we pride ourselves in not closing doors on students who are willing to study. Our pathway options give gauranteed entry into further study."
					
					print(pathway_Amount)
					
					if(pathway_Amount==1):
						pathway_Info= pathway+"For the {} we have one pathway option which I have listed below, please take a look at the course information page linked and let me know if you need more information on this course:<br/><br/>For the {}. You will also be granted gauranteed entry into the {} and all credit that will be applied will be handled automatically by our pathways team.".format(course_Title,pathway_Course,course_Title)
					if(pathway_Amount>1):
						pathway_Info= pathway+"For the {} we have several pathway option which I have listed below, please take a look at the course information page linked and let me know if you need more information on this course:<br/><br/>For the {}. You will also be granted gauranteed entry into the {}and all credit that will be applied will be handled automatically by our pathways team.".format(course_Title,pathway_Course,course_Title)
				else:
					pathway_Info = "Pathway does not exist"
			################################### Scholarships ###################################
			



			scholarship_Info=""
			if (scholarship==True):
				if(international==False):
					ssl._create_default_https_context = ssl._create_unverified_context
					sauce = urllib.request.urlopen("https://www.vu.edu.au/study-at-vu/fees-scholarships/scholarships").read()
					soup = BeautifulSoup(sauce,'lxml')
					results = soup.find('h3').parent.findNext('p').contents
					
					string=""
					
					for x in range(0,len(results)-1):
						string = string+str(results[x])
					string = "<br><br>"+string
					script = Scripts.objects.filter(user=request.user).values('ScholarshipInfo').first()
					scholarship_Info = script['ScholarshipInfo'].replace('/-scholarship-dep-contact-/',string)
				else:
					ssl._create_default_https_context = ssl._create_unverified_context
					sauce = urllib.request.urlopen("https://www.vu.edu.au/study-at-vu/fees-scholarships/scholarships").read()
					soup = BeautifulSoup(sauce,'lxml')
					results = soup.find('h3').parent.findNext('p').findNext('p').findNext('p').contents
					
					string=""
					
					for x in range(0,len(results)-1):
						string = string+str(results[x])
					string = "<br><br>"+string
					script = Scripts.objects.filter(user=request.user).values('ScholarshipInfo').first()
					scholarship_Info = script['ScholarshipInfo'].replace('/-scholarship-dep-contact-/',string)


			################################### Advanced Standing Info ###################################

			advanced_Standing_Info =""

			if(advanced_Standing==True):
				script = Scripts.objects.filter(user=request.user).values('AdvancedStandingInfo').first()
				advancedLink = '<a href="https://www.vu.edu.au/sites/default/files/student-connections/pdfs/A04-application-for-advanced-standing.pdf">Advanced Standing Form</a>'
				advanced_Standing_Info = script['AdvancedStandingInfo']
				advanced_Standing_Info = advanced_Standing_Info.replace('/-advanced-standing-form-/',advancedLink)

			email_String = """
			%s
			%s
			%s
			%s
			%s
			%s
			%s
			%s
			%s
			"""
			script = Scripts.objects.filter(user=request.user).values('HiScript','ThanksScript').first()
			name_String = script['HiScript']
			name_String = name_String.replace("/-first-name-/",name)
			email_link = ("<a href ='{}' class='emaillink'>{}</a>.").format(course_Link,course_Title)
			thanks_String = script['ThanksScript'].replace('/-course-link-/',email_link)
			
			accepted_String = ("{}").format(accepted_Info)
			admission_String = ("{}").format(admission_Info)
			additional_String = ("{}").format(additional_Info)
			advanced_String = ("{}.").format(advanced_Standing_Info)
			scholarship_String = ("{}.").format(scholarship_Info)
			pathway_String = ("{}.").format(pathway_Info)
			close_String = ("{}").format(close_off) 

			return render(
					request,
					'index2.html',
					{'form':form,'name_String':name_String,'thanks_String':thanks_String,'course_Link':course_Link,'course_Title':course_Title,'accepted_Info':accepted_Info,'admission_Info':admission_Info,'additional_Info':additional_Info,'advanced_Standing_Info':advanced_Standing_Info,'scholarship_Info':scholarship_Info,'pathway_Info':pathway_Info,'close_off':close_off,},
				)
		else:
			form = inputForm()
			return render(
				request,
				'index2.html',
				{'form':form,},
			)


	else:
		return HttpResponseRedirect('/profile')
		

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'],first_name=form.cleaned_data['firstname'])
            return HttpResponseRedirect('/login/')
    form = RegistrationForm()
    return render(
    	request,
    	'registration/register.html',
    	{'form':form}
    	)

def home(request):
	return render(
		request,
		'home.html'
		)








