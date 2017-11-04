


$('document').ready(function(){
	var hiscript = document.getElementById('id_HiScript').value
	$('#HiScript').text(hiscript);
	var thanksScript = document.getElementById('id_ThanksScript').value
	$('#ThanksScript').text(thanksScript);
	var applicationDateMature = document.getElementById('id_ApplicationDateMature').value
	$('#ApplicationDateMature').text(applicationDateMature);
	var applicationDateYear12 = document.getElementById('id_ApplicationDateYear12').value
	$('#ApplicationDateYear12').text(applicationDateYear12);
	var applicationDateGeneric = document.getElementById('id_ApplicationDateGeneric').value
	$('#ApplicationDateGeneric').text(applicationDateGeneric);
	var acceptingApplicationsNo = document.getElementById('id_AcceptingApplicationsNo').value
	$('#AcceptingApplicationsNo').text(acceptingApplicationsNo);
	var acceptingApplicationsPG = document.getElementById('id_AcceptingApplicationsPG').value
	$('#AcceptingApplicationsPG').text(acceptingApplicationsPG);
	var acceptingApplicationsINT = document.getElementById('id_AcceptingApplicationsINT').value
	$('#AcceptingApplicationsINT').text(acceptingApplicationsINT);
	var admissionInfo = document.getElementById('id_AdmissionInfo').value
	$('#AdmissionInfo').text(admissionInfo);
	var pathwaysInfo = document.getElementById('id_PathwaysInfo').value
	$('#PathwaysInfo').text(pathwaysInfo);
	var scholarshipInfo = document.getElementById('id_ScholarshipInfo').value
	$('#ScholarshipInfo').text(scholarshipInfo);
	var advancedStandingInfo = document.getElementById('id_AdvancedStandingInfo').value
	$('#AdvancedStandingInfo').text(advancedStandingInfo);
	var close_off_DOM = document.getElementById('id_close_off_DOM').value
	$('#Close_off_DOM').text(close_off_DOM);
	var close_off_INT = document.getElementById('id_close_off_INT').value
	$('#Close_off_INT').text(close_off_INT);
	
});
setTimeout(loader,50)

function loader(){
	var hiscript = $('#HiScript').text()
	$('#id_HiScript').val(hiscript);
	var thanksScript = $('#ThanksScript').text()
	$('#id_ThanksScript').val(thanksScript);
	var applicationDateMature = $('#ApplicationDateMature').text()
	$('#id_ApplicationDateMature').val(applicationDateMature);
	var applicationDateYear12 = $('#ApplicationDateYear12').text()
	$('#id_ApplicationDateYear12').val(applicationDateYear12);
	var applicationDateGeneric = $('#ApplicationDateGeneric').text()
	$('#id_ApplicationDateGeneric').val(applicationDateGeneric);
	var acceptingApplicationsNo = $('#AcceptingApplicationsNo').text()
	$('#id_AcceptingApplicationsNo').val(acceptingApplicationsNo);
	var acceptingApplicationsPG = $('#AcceptingApplicationsPG').text()
	$('#id_AcceptingApplicationsPG').val(acceptingApplicationsPG);
	var acceptingApplicationsINT = $('#AcceptingApplicationsINT').text()
	$('#id_AcceptingApplicationsINT').val(acceptingApplicationsINT);
	var admissionInfo = $('#AdmissionInfo').text()
	$('#id_AdmissionInfo').val(admissionInfo);
	var pathwaysInfo = $('#PathwaysInfo').text()
	$('#id_PathwaysInfo').val(pathwaysInfo);
	var scholarshipInfo = $('#ScholarshipInfo').text()
	$('#id_ScholarshipInfo').val(scholarshipInfo);
	var advancedStandingInfo = $('#AdvancedStandingInfo').text()
	$('#id_AdvancedStandingInfo').val(advancedStandingInfo);
	var close_off_DOM = $('#Close_off_DOM').text()
	$('#id_close_off_DOM').val(close_off_DOM);
	var close_off_INT = $('#Close_off_INT').text()
	$('#id_close_off_INT').val(close_off_INT);
};
// just querying the DOM...like a boss!
var links = document.querySelectorAll(".itemLinks");
var wrapper = document.querySelector("#wrapper");
 
// the activeLink provides a pointer to the currently displayed item
var activeLink = 0;
 
// setup the event listeners
for (var i = 0; i < links.length; i++) {
    var link = links[i];
    link.addEventListener('click', setClickedItem, false);
 
    // identify the item for the activeLink
    link.itemID = i;
}
 
// set first item as active
links[activeLink].classList.add("active");
 
function setClickedItem(e) {
    removeActiveLinks();
 
    var clickedLink = e.target;
    activeLink = clickedLink.itemID;
 
    changePosition(clickedLink);
}
 
function removeActiveLinks() {
    for (var i = 0; i < links.length; i++) {
        links[i].classList.remove("active");
    }
}
 
// Handle changing the slider position as well as ensure
// the correct link is highlighted as being active
function changePosition(link) {
    var position = link.getAttribute("data-pos"); 
 	clicker = parseInt(position)
    var translateValue = "translate3d(" + position + ", 0px, 0)";
    wrapper.style.transform = translateValue;
    link.classList.add("active");
}

var clicker = 0

$(function(){
	checker();
	$('.left').click(function(){
		if(0>clicker){
			clicker=clicker+550
			clickerpx=clicker+"px"
			translater = "translate3d(" + clickerpx + ", 0px, 0)";
			wrapper.style.transform = translater
		} 
	})

	$('.right').click(function(){
		if(clicker>-2200){
			clicker=clicker-550
			clickerpx=clicker+"px"
			translater = "translate3d(" + clickerpx + ", 0px, 0)";
			wrapper.style.transform = translater;
		} 
	})
});
function checker(){
	if(clicker>-2200 && clicker<-0){
		right.style.opacity = 1
		left.style.opacity = 1

	}else{
		if (clicker==-2200){
			right.style.opacity = 0.5
		}else if (clicker==0){
			left.style.opacity = 0.5
		}
	}
	setTimeout(checker,50);
}




