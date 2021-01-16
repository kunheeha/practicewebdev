$(document).ready(function () {
	var shapeInput = $("#inputShape");

	$(".getShape").on("click", function() {
		
		
		$.ajax({
			type: 'POST',
			url: '/',
			data: {"shapeInput":shapeInput.val()},
			success: function(data) {
				if (data == 'no') {
					alert("I cant make that shape sorry..");
				} else {
					window.location.href = "/" + data;
				}
			},
			error: function() {
				console.log("It didn't work")
			}
		});
	})

});