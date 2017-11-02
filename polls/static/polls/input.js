
$('#international').click(function(event){
	if(document.getElementById('#id_international').checked){
		window.alert("hello")
	}else{
		$('#id_international').prop("checked",true)
	}
})