   		function err_mesg(inp, err) {
            if ($(inp).next(".validation").length == 0) { // only add if not added
                $(inp).css("background-color", "#FFBABA");
                    $(inp).after("<div class='validation' style='color:red;margin-bottom: 5px;'>" + err + "</div>");
            }
        }

$("input").click(function() {
  removeVal(this);
});
$("input").change(function() {
  removeVal(this);
});

function removeVal(inp) {
  $(inp).css("background-color", "");
    $(inp).next(".validation").remove();
}

		jQuery(document).ready(function() {
			jQuery('#example').DataTable({
				"searching": false,
				"paging": true,
				"info": false,
				"lengthChange":false
			});

		})

		$('#disablebuttone').click(function(){			
			if($('#startup-email').prop('disabled')){
			 $('#startup-email').prop('disabled', false)
			}
			else{
			 $('#emp-email').prop('disabled', true)
			}
		});
		$('#disablebuttonp').click(function(){
			if($('#startup-contact').prop('disabled')){
			 $('#startup-contact').prop('disabled', false)
			}
			else{
			     $('#phone-number').prop('disabled', true)
			  }
		});

		$('#btn-save-profile').click(function(){
			var id = $("#startup-id").val();			
			var emp_email = $("#startup-email").val();
			var phone_number = $("#startup-contact").val();
			var err = false;
            if (phone_number.length < 11 || phone_number.length > 13) {
                err_mesg("#startup-contact", "Enter a valid mobile phone");
                if (!err) {
                    err = true;
                    $("#startup-contact").focus();
                }
            }
            var email_sp = $("#startup-email").val().split("@");
            if (email_sp.length !== 2 || email_sp[1].split(".").length < 2) {
                err_mesg("#startup-email", "Enter a valid email");
                if (!err) {
                    err = true;
                    $("#startup-email").focus();
                }
            }
			if (!err){
				$.ajax({
		               url: '/startup/analytics/profile/ajax',
		               type: 'POST',
		               dataType: 'json',
		               data: {
		                  'id': id,
		                  'emp_email' : emp_email,
		                  'phone_number' : phone_number,
		                  'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
		               },
		               success: function(data){
		              if (data.form_is_valid){
		                alert('Email and Phone Number updated.')
		              }else{
		                alert('Failed to update.')
		              }
		            }            
		        })//end ajax	
			}
		}) //save-btn-profile