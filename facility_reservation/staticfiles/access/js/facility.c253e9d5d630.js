$(document).ready(function() {
  get_expected();
  get_loggedin();
  get_arriving(); 
  $('#tb1').DataTable({
    order: [[ 2, "desc" ]],
    lengthMenu: [[5, 10, 25, 50], [5, 10, 25, 50]],
    columnDefs: [
        { orderable: false,
          searchable: false,
            className: "center",
            // targets: [5, 6, 7, 9]
            targets: [1, 2, 3]
        },
      {
        data: 'booking_id',
        targets: [0]
      },
      {
        data: 'client__username',
        targets: [0]
      },
      {
        data: 'client__first_name',
        targets: [1]
      },
      {
        data: 'client__last_name',
        targets: [2]
      },
      {
        data: 'client__groups',
        targets: [3]
      },
      {
        targets: [4],
        data: null,
        render: function ( data, type, row ) {
            return '<!-- Button trigger modal --><button type="button" class="btn btn-sm btnView w-100" data-toggle="modal" data-target="#view">View</button>';
          }
      },
      // {
      //   data: 'duration',
      //   targets: [5]
      // },
      // {
      //   data: 'program',
      //   targets: [6]
      // },
      // {
      //   data: 'year',
      //   targets: [7]
      // },
      // {
      //   data: 'facility',
      //   targets: [8]
      // },
      // {
      //   data: 'techno',
      //   targets: [9]
      // },
    ],
    searching: true,
    processing: true,
    serverSide: true,
    stateSave: true,
    ajax: 'ajax/facility_access_table',
    "responsive": true,
    "scrollX": true,
    "dom": 'lfrtip',
  });
});

$("#ex_spaces").change(function() {
  get_expected();
})

function get_expected() {
  var venue = $("#ex_spaces option:selected").text().trim();
  $.ajax({
      url: 'ajax/get_expected',
      data: {
        'venue': venue,
      },
      success: function(data) {
        $("#ex_incubatees").text(data.incubatee);
        $("#ex_techno").text(data.techno)
        $("#ex_others").text(data.others)
      },
  });
}

$("#lo_spaces").change(function() {
  get_loggedin();
})

function get_loggedin() {
  var venue = $("#lo_spaces option:selected").text().trim();
  $.ajax({
      url: 'ajax/get_loggedin',
      data: {
        'venue': venue,
      },
      success: function(data) {
        $("#lo_incubatees").text(data.incubatee);
        $("#lo_techno").text(data.techno)
        $("#lo_others").text(data.others)
      },
  });
}

$("#ar_spaces").change(function() {
  get_arriving();
})

function get_arriving() {
  var venue = $("#ar_spaces option:selected").text().trim();
  $.ajax({
      url: 'ajax/get_arriving',
      data: {
        'venue': venue,
      },
      success: function(data) {
        $("#ar_incubatees").text(data.incubatee);
        $("#ar_techno").text(data.techno)
        $("#ar_others").text(data.others)
      },
  });
}