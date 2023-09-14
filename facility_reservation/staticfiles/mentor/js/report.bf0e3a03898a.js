$("#book-from").change(function() {
	date_filter();
});
$("#book-to").change(function() {
	date_filter();
});
function b_ongoing() {
	var today = new Date();
    var mon = (today.getMonth()+1);
    if (mon < 10) {
        mon = "0" + mon;
    }
    var date = today.getFullYear()+'-'+mon+'-'+today.getDate();
	reset_book(date, date, false);
}
function b_upcoming() {
	var today = new Date();
    var mon = (today.getMonth()+1);
    if (mon < 10) {
        mon = "0" + mon;
    }
    var date = today.getFullYear()+'-'+mon+'-'+today.getDate();
	reset_book(date, '2099-12-31', false);
}
function b_all() {
	reset_book('2020-01-01', '2099-12-31', false);
}
function b_done() {
	var today = new Date();
    var mon = (today.getMonth()+1);
    if (mon < 10) {
        mon = "0" + mon;
    }
    var date = today.getFullYear()+'-'+mon+'-'+today.getDate();
	reset_book('2020-01-01', date, false);
}
function date_filter() {
	var from = $("#book-from").val();
	var to = $("#book-to").val();
	reset_book(from, to, true);
}
function ment_change() {
	var from = $("#ment-from").val();
	var to = $("#ment-to").val();
	if (from == "") {
		err_mesg($("#ment-from"), "This field is required");
	} else if (to == "") {
		err_mesg($("#ment-to"), "This field is required");
	} else if (from > to) {
		err_mesg($("ment-to"), "Date to must be after Date from");
	} else {
		$("#reportTbl2").DataTable().destroy();
		$('#reportTbl2').DataTable({
			language: lang,
            order: [[ 0, "desc" ]],
            lengthMenu: [[5, 10, 25, 50], [5, 10, 25, 50]],
            columnDefs: [
                {orderable: false,
                 searchable: true,
                 className: "center",
                 targets: [4, 5, 7, 8]
                },
                {
                    data: 'username',
                    targets: [0]
                },
                {
                    data: 'first_name',
                    targets: [1]
                },
                {
                    data: 'last_name',
                    targets: [2]
                },
                {
                    data: 'expertise',
                    targets: [3]
                },
                {
                    data: 'schedule',
                    targets: [4]
                },
                {
                    data: 'rating',
                    targets: [5]
                },
                {
                    data: 'academe',
                    targets: [6]
                },
                {
                    data: 'total_hrs',
                    targets: [7]
                },
                {
                    data: 'mentees',
                    targets: [8]
                }
            ],
            searching: true,
            processing: true,
            serverSide: true,
            stateSave: true,
            ajax: 'ajax/all_mentors/'+from+'/'+to+'/',
            "responsive": true,
            "scrollX": true,
            "dom": '<"row"<"col-12"<"tbl2-header"<"row"<"col-12 col-xl-10 tbl2-header-left"><"col-12 col-xl-2 tbl2-header-right"B>>>>>tip',
            buttons: [
                {extend: 'excel', text: 'Export Now', filename: "Mentors", className: 'btn-export'},
            ],
		});
		$("div.dataTables_info").addClass('d-flex justify-content-center');
        $("div.tbl2-header-left").addClass("d-flex justify-content-start");
        $("div.tbl2-header-right").addClass("d-flex justify-content-start align-items-center");
        $("div.tbl2-header-left").append('<div class="form-group form-inline" style="padding-left:5px;"><label>From: <input class="form-control form-control-sm" type="date" style="width:120px" id="ment-from" onchange="ment_change()"></label></div>');
        $("div.tbl2-header-left").append('<div class="form-group form-inline" style="padding-left:15px;"><label>To: <input class="form-control form-control-sm" type="date" style="width:120px" id="ment-to" onchange="ment_change()"></label></div>');
	}
}

function reset_book(from, to, appear) {
    if (from == ""){
        from = " ";
    }
    if (to == "") {
        to = " ";
    }
	$("#reportTbl1").DataTable().destroy();
		$('#reportTbl1').DataTable({
			language: lang,
            order: [[ 0, "desc" ]],
            lengthMenu: [[5, 10, 25, 50], [5, 10, 25, 50]],
            columnDefs: [
                {orderable: false,
                 searchable: true,
                 targets: [7]
                },
                {
                    data: 'id',
                    targets: [0]
                },
                {
                    data: 'mentor',
                    targets: [1]
                },
                {
                    data: 'individual',
                    targets: [2]
                },
                {
                    data: 'schedule',
                    targets: [3]
                },
                {
                    data: 'duration',
                    targets: [4]
                },
                {
                    data: 'venue',
                    targets: [5]
                },
                {
                    data: 'description',
                    targets: [6]
                },
                {
                    data: 'team',
                    targets: [7]
                },
                {
                    data: 'cost',
                    targets: [8]
                },
                {
                    data: 'status',
                    targets: [9]
                }
            ],
            searching: true,
            processing: true,
            serverSide: true,
            stateSave: true,
            ajax: 'ajax/all_bookings/' + from + '/' + to + '/',
            "responsive": true,
            "scrollX": true,
            "dom": '<"row"<"col-12"<"tbl1-header"<"row"<"col-12 col-xl-6 tbl1-header-left"f><"col-12 col-xl-6 tbl1-header-right"B>>>>>tip',
            buttons: [
                {extend: 'excel', text: 'Export Now', filename: "MentorBookings", className: 'btn-export'},
            ],
		});
		$("div.dataTables_info").addClass('d-flex justify-content-center');
        $("div.tbl1-header-left").addClass("d-flex justify-content-start");
        $("div.tbl1-header-right").addClass("d-flex justify-content-start align-items-center");
        if (appear) {
            $("div.tbl1-header-left").append('<div style="padding-left:5px;"><input class="form-control form-control-sm" type="date" style="width:120px" id="book-from" onchange="date_filter()" value="'+from+'"></div>');
            $("div.tbl1-header-left").append('<div style="padding-left:5px;"><input class="form-control form-control-sm" type="date" style="width:120px" id="book-to" onchange="date_filter()" value="'+to+'"></div>');
        } else {
            $("div.tbl1-header-left").append('<div style="padding-left:5px;"><input class="form-control form-control-sm" type="date" style="width:120px" id="book-from" onchange="date_filter()"></div>');
            $("div.tbl1-header-left").append('<div style="padding-left:5px;"><input class="form-control form-control-sm" type="date" style="width:120px" id="book-to" onchange="date_filter()"></div>');    
        }
        $("div.tbl1-header-right").prepend('<label style="font-size:20px; padding-left:5px"><a href="javascript:void(0);" onclick="b_all()" style="color:black"><b>ALL</b></a></label>');
        $("div.tbl1-header-right").prepend('<label style="font-size:20px; padding:0px 5px 0px 5px; border-right: 1px solid #000030"><a href="javascript:void(0);" onclick="b_done()" style="color:black"><b>DONE</b></a></label>');
        $("div.tbl1-header-right").prepend('<label style="font-size:20px; padding:0px 5px 0px 5px; border-right: 1px solid #000030"><a href="javascript:void(0);" onclick="b_upcoming()" style="color:black"><b>UPCOMING</b></a></label>');
        $("div.tbl1-header-right").prepend('<label style="font-size:20px; padding:0px 5px 0px 10px; border-right: 1px solid #000030"><a href="javascript:void(0);" onclick="b_ongoing()" style="color:black"><b>ON-GOING</b></a></label>');
}

function override(id) {
    $.ajax({
        url: 'ajax/override_lp',
        data: {
            'id': id,
        },
        dataType: 'json',
        success: function() {
            alert("Override successful");
            $('#reportTbl1').DataTable().ajax.reload();
        }
    });
}

function reject(id) {
    $.ajax({
        url: 'ajax/cancel_booking',
        data: {
            'id': id,
        },
        dataType: 'json',
        success: function() {
            alert("Booking cancelled successfully");
            $('#reportTbl1').DataTable().ajax.reload();
        }
    });
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

function err_mesg(inp, err) {
	if ($(inp).next(".validation").length == 0) { // only add if not added
		$(inp).css("background-color", "#FFBABA");
        $(inp).after("<div class='validation' style='color:red;margin-bottom: 5px;'>" + err + "</div>");
    }
}