var added_stud = [];
function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*for each item in the array...*/
      for (i = 0; i < arr.length; i++) {
        /*check if the item starts with the same letters as the text field value:*/
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase() && !added_stud.includes(arr[i])) {
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          b.setAttribute("style", "font-weight: normal; font-size: 0.85rem;")
          /*make the matching letters bold:*/
          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
          /*execute a function when someone clicks on the item value (DIV element):*/
          b.addEventListener("click", function(e) {
            /*insert the value for the autocomplete text field:*/
            name = this.getElementsByTagName("input")[0].value;
            $(inp).val("");
            closeAllLists();
            added_stud.push(name);
            reload_chart();
          });
          a.appendChild(b);
        }
      }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed, prevent the form from being submitted,*/
        e.preventDefault();
        if (currentFocus > -1) {
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
      x[i].parentNode.removeChild(x[i]);
    }
  }
}
/*execute a function when someone clicks in the document:*/
document.addEventListener("click", function (e) {
    closeAllLists(e.target);
});
}

$("input[name=render]").change(function() {
    reload_chart();
});
$("input[name=data]").change(function() {
    reload_chart();
});

$(".util-dates").change(function() {
    reload_chart();
});

$(document).ready(function() {
  reload_chart();

  $("#example").dataTable({
    dom: "frtipB",
    buttons: [
      {extend: 'excel', action: newExportAction, text: 'Export Now', filename: "Startup Details", className: 'btn-export'},
    ],
    order: [0, "desc"],
    columnDefs: [
          {
            orderable: false,
            searchable: false,
            className: "",
            targets: [1,2,3,4,5,6]
          },
      {
        data: 'name',
        targets: [0]
      }, 
      {
        data: 'mos_customer',
        targets: [1]
      }, 
      {
        data: 'mos_revenue',
        targets: [2]
      }, 
      {
        data: 'engagement',
        targets: [3]
      }, 
      {
        data: 'turnover',
        targets: [4]
      }, 
      {
        data: 'technology',
        targets: [5]
      }, 
      {
        data: 'investment',
        targets: [6]
      }
    ],
      searching: true,
      processing: true,
      serverSide: true,
      stateSave: true,
    ajax: 'ajax/view_startup_dash'
  });
})

var chart;

function reload_chart() {
  var render = $("input[name=render]:checked").val();
  var _data = $("input[name=data]:checked").val();
  $.ajax({
    url: 'ajax/view_dash_util_chart',
    data: {
      'employees': added_stud.toString(),
      'startups': added.toString(),
      'data': _data,
      'render': render,
      'from': $("#util-from").val(),
      'to': $("#util-to").val(),
    },
    success: function(data) {
      var all_data = [];
      for (i = 0; i < added.length + added_stud.length; i++) {
        var all_x = data.x.split("|")[i]
        var all_y = data.y.split("|")[i]
        var xs = all_x.split(",")
        var ys = all_y.split(",")
        var datapoints = []
        for (j = 0; j < xs.length; j++) {
          var x = xs[j];
          var date = new Date(x.split(" ")[2], parseInt(x.split(" ")[0])-1, x.split(" ")[1]);
          var dict = {
            x: date,
            y: parseInt(ys[j])
          }
          datapoints.push(dict);
        };
        if (i < added.length) {
          var my_data = {
            type: "line",
            showInLegend: true,
            name: added_name[i].toString(),
            dataPoints: datapoints,
          };
        } else {
          var my_data = {
            type: "line",
            showInLegend: true,
            name: added_stud[i-added.length].toString(),
            dataPoints: datapoints,
          };
        }
        all_data.push(my_data);
      }
      var ax_y = {
        crosshair: {
          enabled: true,
        }
      };
      var title = "";
      if (_data == "points") {
        title = "Points";
      } else if (_data == "coins") {
        title = "Coins";
      } else if (_data == "internet"){
        title = "Internet (in Mb)";
      }
      ax_y.title = title;
      chart = new CanvasJS.Chart("chart", {
        animationEnabled: true,
        theme: "light2",
        title:{
          text: "Startup Utilization"
        },
        axisX:{
          valueFormatString: "DD MMM YY",
          crosshair: {
            enabled: true,
            snapToDataPoint: true
          }
        },
        legend:{
          cursor:"pointer",
          verticalAlign: "bottom",
          horizontalAlign: "left",
          dockInsidePlotArea: false,
          itemclick: toogleDataSeries
        },
        axisY:ax_y,
        toolTip:{
          shared:true
        },
        data: all_data,
      });
      chart.render();
      $(".canvasjs-chart-credit").remove();
    },
  });
}

function toogleDataSeries(e){
  if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
    e.dataSeries.visible = false;
  } else{
    e.dataSeries.visible = true;
  }
  chart.render();
  $(".canvasjs-chart-credit").remove();
}