$(document).ready(function(){
    $('.sidenav').sidenav({
		edge: "right",
		closeOnClick: true,
	});
    $('.collapsible').collapsible();
    $('.fixed-action-btn').floatingActionButton();
    $('.modal').modal();
});

$('img').on('error', () => {
    $(this).attr('src', '/static/images/avatar_default.jpg');
})