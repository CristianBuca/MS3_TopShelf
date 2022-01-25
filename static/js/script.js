// MaterializeCSS initializations
$('.sidenav').sidenav({
    edge: "right",
    closeOnClick: true,
});
$('.collapsible').collapsible();
$('.fixed-action-btn').floatingActionButton();
$('.modal').modal();

// Credit for use of Ajax to replace broken images to my mentor
// Mo Shami and https://www.sitepoint.com/jquery-replace-broken-images/

$("img").each( function () 
{
	var _this = $(this);
	
	$.ajax({
		url:$(this).attr('src'),
		type:'HEAD',
		async: true,
		error:
			function(e)
			{
				if (e.status == '404') {
					$(_this).attr('src', '/static/images/avatar_default.jpg');
				}
			}
	});
});