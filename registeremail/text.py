Thanks script 
	"Thank you for your enquiry regarding the  <a href ='{}' class='emaillink'>{}</a>."


APPLICATION DATES:

		If student is mature age

		"It is great that you are considering furthering your education. We are currently accepting applications for this course and would be happy to see you apply. Judging by your past educational and work experience you would be classed as a mature age student, all mature age students are more than welcome to submit your application directly online. Online applications close on the <b>{}</b>\n".

		If student is year 12 

		"It is great that you are considering studying with Victoria University. We are currently accepting applications for this course and would be happy to see you apply. Since you are a 12th grade applicant you can apply through VTAC until <b>{}</b>.\n".format(bold[0].text,bold[1].text)


		If student is generic
		"It is great that you are considering studying with Victoria University. We are currently accepting applications for this course and would be happy to see you apply. If you are a 12th grade applicant you can apply through VTAC until <b>{}</b>, otherwise you are more than welcome to submit your application directly through us by submitting an online application. Online applications close on the <b>{}</b>\n".format(bold[0].text,bold[1].text)

Accepting Applications 
		If no:
		"Applications for this course are not being taken at this time. However we may be considering applications in the future, please check the following website link and check back to see if we are considering students in the future. I have still tried my best to answer your questions, please let me know if you require more information."
		If POST GRAD (OR ONLY TAKES MATURE): 
		"It is great that you are considering furthering your education. We are currently accepting applications for this course and would be happy to see you apply. You are more than welcome to submit your application directly through us by submitting an online application. Online applications close on the <b>{}</b>\n"	
		
		If student is International 
			 "We are currently accepting applications for this course. As an international student you can apply directly to VU using our online application, or alternatively you can submit an application through an education agent."
			


Admission information:
	"In order to apply for this course you will need to satisfy the following entry requirements.\n{}"


Pathway information:

"It is ok if you do not meet those requirements, we pride ourselves in not closing doors on students who are willing to study. Our pathway options give gauranteed entry into further study."

	
		"For the {} we have one pathway option which I have listed below, please take a look at the course information page linked in each pathway and let me know if you need more information on these courses:<br/><br/>For the {}. You will also be granted gauranteed entry into the {} and all credit that will be applied will be handled automatically by our pathways team."

Scholarship information DOMESTIC:

"VU has a huge range of scholarship options, however they are distributed based on certain factors and therefore each students eligibility will vary. I have provided you with details below for the relevant scholarships department:{}"

Advanced Standing application

"If you have completed any of this course previously at another university, you may be eligible for credit. In order to assess your credit you will need to complete an <a href='https://www.vu.edu.au/sites/default/files/student-connections/pdfs/A04-application-for-advanced-standing.pdf'>Advanced Standing Application form</a> along with your course application. If you receive an offer then we can assess your credit and advise you of how much your study will be reduced by.""



Close off
	If student is domestic 
	"I hope I have been able to answer most of your questions {} about the {}. If you have any other questions please feel free to contact me by responding to this email, or by calling us on 03 9919 6100<br/><br/>Kind regards,<br/>Dimitri <br/>Student Service Officer, VUHQ<br/>Phone +61 3 9919 6100 <br/>For additional information, please visit <a href='https://askvu.vu.edu.au/'>ASKVU</a>".format(name,course_Title)

	If student is International 
	"I hope I have been able to answer most of your questions {} about the {}.As an international applicant you are more than welcome to contact our Victoria University International Office directly for relevant information and application assistance. Their details are listed below:<br/><br/>Web: <a href='http://www.vu.edu.au/international/'>http://www.vu.edu.au/international/</a><br/>Email: international@vu.edu.au<br/>Phone: +61 3 9919 1164<br/><br/>If for some reason you have any other questions please let me know by responding to this email! <br/><br/>Kind regards,<br/>Dimitri <br/>Student Service Officer, VUHQ<br/>Phone +61 3 9919 6100 <br/>For additional information, please visit <a href='https://askvu.vu.edu.au/'>ASKVU</a>"



