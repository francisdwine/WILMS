$(".remove").click(function(event) {
	event.preventDefault();	
	console.log(event.target.id.substring(3));
	$(event.target).parent().find(".star-ratings-rating-foreground").css("width", "0%");
	$.ajax({
		url: 'ajax/rem_rate',
		data: {
			'exp': event.target.id.substring(3),
   			'id': user,
   		},
   		dataType: 'json',
	});
});

// $(".star-ratings-rate-action").each(function() {
// 	$(this).children("button").attr("type", "button");
// })
// 
$("li").click(function(event) {
	var exp = $(event.target).parent().parent().parent().parent().parent().parent().get(0).id.substring(3);
	var score = $(event.target).attr("data-score");
	console.log(score);
	console.log(exp);
	$.ajax({
		url: 'ajax/upd_rate',
		data: {
			'score': score,
			'exp': exp,
   			'id': user,
   		},
   		dataType: 'json',
	});
	// $(this).parent().children().each(function(index) {
	// 	console.log(index);
	// 	if (index < score) {
	// 		$(this).find("button").attr("class", "star-ratings-rating-full");
	// 	} else {
	// 		$(this).find("button").attr("class", "star-ratings-rating-empty");
	// 	}
	// });
});

$(document).ready(function() {
	$(".star-ratings-rating-average").hide();
	$(".star-ratings-rating-count").hide();
	$(".star-ratings-rating-user").hide();
	$("li").css("height", "20px");
	$(".star-ratings").css("top", "10px");
});