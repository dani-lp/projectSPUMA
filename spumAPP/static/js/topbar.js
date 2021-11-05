let extended = false;

const processTopbarState = () => {
    if (extended) {
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
    extended = !extended;
    processTopbarState();
});

$('.topbar-anchor').click(function() {
    extended = false;
    processTopbarState();
});