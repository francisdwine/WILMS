$("input[name=sat-render]").change(function() {
  more_details(false);
});

$("#customersatfrom").change(function() {
  get_vensat();
});

$("#customersatto").change(function() {
  get_vensat();
});

function get_vensat() {
  var from = $("#customersatfrom").val();
  var to = $("#customersatto").val();
  $.ajax({
    url: 'ajax/get_vensat',
    data: {
      'from': from,
      'to': to,
    },
    success: function(data) {
      $("#custsatis").text(data.data);
    },
  });
}

function more_details(disp) {
  var render = $("input[name=sat-render]:checked").val();
  var from = $("#customersatfrom").val();
  var to = $("#customersatto").val();
  $.ajax({
    url: 'ajax/more_vensat',
    data: {
      'render': render,
      'from': from,
      'to': to,
    },
    success: function(data) {
      var xs = data.x.split(",")
      var ys = data.y.split(",")
      var datapoints = []
      for (j = 0; j < xs.length; j++) {
        var x = xs[j];
        var date = new Date(x.split(" ")[2], parseInt(x.split(" ")[0])-1, x.split(" ")[1]);
        var dict = {
          x: date,
          y: parseFloat(ys[j])
        }
        datapoints.push(dict);
      };
      var chart = new CanvasJS.Chart("sat-chart", {
        animationEnabled: true,
        theme: "light2",
        title:{
          text: "Mentor Ratings"
        },
        axisX:{
          valueFormatString: "DD MMM YY",
          crosshair: {
            enabled: true,
            snapToDataPoint: true
          }
        },
        axisY: {
          crosshair: {
            enabled: true,
          },
          title: "Average Rating",
          maximum: 5,
          minimum: 1,
        },
        toolTip:{
          shared:true
        },
        data: [
          {
            type: "line",
            showInLegend: true,
            name: "Rating",
            dataPoints: datapoints,
          }
        ],
      });
      chart.render();
      $(".canvasjs-chart-credit").remove();
    },
  });
  if (disp) {
    $("#more-sat").modal("show");
  }
}