// Menu dropdown
let menuExtended = false;

const processMenuState = () => {
    if (menuExtended) {
        $('#topbar-menu-collapse').css('height', '100%');
        $('.topbar-collapse-container').css({ 
            opacity: 1, 
            'display': 'flex' 
        });
    } else {
        $('#topbar-menu-collapse').css('height', '0');
        $('.topbar-collapse-container').css({ 
            opacity: 0, 
            'display': 'none' 
        });
    }
}

$('#topbar-menu-toggle').click(function() {
    menuExtended = !menuExtended;
    processMenuState();
});

$('.topbar-anchor').click(function() {
    menuExtended = false;
    processMenuState();
});

$(document).on('click', function (e) {
    if(
        $(e.target).closest('#topbar-menu-collapse').length == 0 &&
        $(e.target).closest('#topbar-menu-toggle').length == 0 &&
        menuExtended
    ) {
        menuExtended = false;
        processMenuState();
    }
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