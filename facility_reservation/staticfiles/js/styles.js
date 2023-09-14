/**Booking Form**/

var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
  // This function will display the specified tab of the form ...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  // ... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    $("#nextBtn").hide();
    $("#p_coins").show();
    $("#p_points").show();
      $.ajax({
          url: 'ajax/book',
          async: false,
          data: {
            'venue': venue,
            'from': selFrom.toString(),
            'to': selTo.toString(),
            'description': $("#desc").val(),
            'purpose': $("#purpose option:selected").val(),
            'attendees': $("#ids").val(),
            'computers': $("#computers").val()
          },
          dataType: 'json',
          success: function(data) {
            $("#fin_refNo").val(data.refNo);
            $("#fin_attendees").val($("#names").val());
            $("#fin_facilities").val(venue);
            $("#fin_date").val(data.date);
            $("#fin_time").val(data.time);
            $("#fin_cost").val(data.cost);
          }
      });
  } else {
    $("#nextBtn").show();
    $("#p_coins").hide();
    $("#p_points").hide();
  }
  // ... and run a function that displays the correct step indicator:
  fixStepIndicator(n)
}

function pay(method) {
  $.ajax({
    'url': 'ajax/pay_booking',
    'data': {
      'method': method,
    },
    success: function(data) {
      if (data.err == '') {
        alert("Booking successful!");
        $("#book").modal("hide");
        location.reload();
      } else {
        alert(data.err);
      }
    },
  });
}

function resetView() {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Hide the current tab:
  x[1].style.display = "none";
  x[2].style.display = "none";
  currentTab = 0;
  showTab(0);
}

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  if (currentTab + n + 1 == x.length) {
    console.log("Validity Check Active");
    var err = "";
    $.ajax({
      async: false,
      url: 'ajax/validity_check',
      data: {
        'venue': venue,
        'from': selFrom.toString(),
        'to': selTo.toString(),
        'attendees': $("#ids").val(),
        'computers': $("#computers").val()
      },
      success: function(data) {
        err = data.err;
        $("#error").val(data.err);
      }
    });
    if (err == "") {
      currentTab = currentTab + n;
    }
    console.log("Check done");
  } else {
    currentTab = currentTab + n;
  }
  // if you have reached the end of the form... :
  if (currentTab >= x.length) {
    //...the form gets submitted:
    // document.getElementById("regForm").submit();
    return false;
  }
  // Otherwise, display the correct tab:
  showTab(currentTab);
}

function checkIfValid() {
  console.log("VALIDITY CHECK ACTIVE");
  var err = "";
    return err;
}

function validateForm() {
  // This function deals with validation of the form fields
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");
  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "" && y[i].required) {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false:
      valid = false;
    }
  }
  // If the valid status is true, mark the step as finished and valid:
  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
  }
  return valid; // return the valid status
}

function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  //... and adds the "active" class to the current step:
  x[n].className += " active";
}