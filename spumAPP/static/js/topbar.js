let menuExtended = false;

const processTopbarState = () => {
    if (menuExtended) {
        $('.topbar-menu-collapse').css('height', '100%');
        $('.topbar-collapse-container').css({ 
            opacity: 1, 
            'display': 'flex' 
        });
    } else {
        $('.topbar-menu-collapse').css('height', '0');
        $('.topbar-collapse-container').css({ 
            opacity: 0, 
            'display': 'none' 
        });
    }
}

$('#topbar-menu-toggle').click(function() {
    menuExtended = !menuExtended;
    processTopbarState();
});

$('.topbar-anchor').click(function() {
    menuExtended = false;
    processTopbarState();
});


// User dropdown
let userExtended = false;

$('#topbar-user-toggle').click(function(e) {
    userExtended = !userExtended;

    if(userExtended) {
        $('#topbar-user-dropdown').css('display', 'flex');
    } else {
        $('#topbar-user-dropdown').css('display', 'none');
    }
});

$(document).on('click', function (e) {
    if(
        $(e.target).closest('#topbar-user-dropdown').length == 0 &&
        $(e.target).closest('#topbar-user-toggle').length == 0 &&
        userExtended
    ) {
        $('#topbar-user-dropdown').css('display', 'none');
        userExtended = false;
    }
});