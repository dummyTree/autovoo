function onloader(){
	alert('hello')
}


$(function(){

	$('label[for=id_international]').click(function(){
		$('label[for=id_international]').toggleClass('colored')
	})
	$('label[for=id_pathways]').click(function(){
		$('label[for=id_pathways]').toggleClass('colored')
	})

	$('label[for=id_scholarship]').click(function(){
		$('label[for=id_scholarship]').toggleClass('colored')
	})
	$('label[for=id_advancedstanding]').click(function(){
		$('label[for=id_advancedstanding]').toggleClass('colored')
	})

	$('label[for=id_year12]').click(function(){
		$('label[for=id_year12]').toggleClass('colored')
	})
	$('#submit').click(function(){
		$('.input-sub-container').addClass('colouring')
	})
})