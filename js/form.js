// $(document).ready(function() {
// 	if (jQuery) {
// 		// jQuery is loaded
// 		alert("Yeah!");
// 	} else {
// 		// jQuery is not loaded
// 		alert("Nooo!");
// 	}
// });

$(document).ready(function(){

	$("#contact-form").submit( function(event) {
		
		var is_error = false;
		var error_count = 0;

		var fullname = $("#fullname").val();
		if(fullname == ""){
			$("input#fullname").css("border-color", "#632203");
			is_error = true;
			error_count += 1;
		}

		var address = $("#address").val();
		if(address ==""){
			$("input#address").css("border-color", "#632203");
			is_error = true;
			error_count +=1;
		}


		var number = $("#number").val();
		if(number == ""){
			$("input#number").css("border-color","#632203");
			is_error = true;
			error_count += 1;
		}


		var email = $("#email").val();
		if(email == ""){
			$("input#email").css("border-color", "#632203");
			is_error = true;
			error_count += 1;
		}

		var description = $("#description").val();
		if(description == ""){
			$("textarea#description").css("border-color", "#632203");
			is_error = true;
			error_count += 1;
		}

		if (is_error == true){
			$("span#error-count").text(error_count);
			$("p#error-list").css("display", "block");
			event.preventDefault();
		}
	});

	$("#fullname").focusout(function() {
		$("input#fullname").css("border-color", "#F3EEED");
	});

	$("#fullname").focuscount(function() {
		$("input#address").css("border-color", "#F3EEED");
	});

	$("#number").focusout(function() {
		$("input#number").css("border-color", "#F3EEED");
	});

	$("#email").focusout(function() {
		$("input#email").css("border-color", "#F3EEED");
	});
	$("#description").focusout(function() {
		$("textarea#description").css("border-color", "#F3EEED");
	});
});
