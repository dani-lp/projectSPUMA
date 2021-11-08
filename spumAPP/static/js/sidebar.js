const $sidebar = $('#home-sidebar');
let isExtended = true;

const processSidebarState = () => {
    if (isExtended) {
        $('#sidebar-button').css('transform', 'rotateY(180deg)');
        $('.sidebar-plugin').css('display', 'block');
        $('#sidebar-title').css('display', 'block');
        $('#home-sidebar').css('width', '340px');
        $('.dashboard-container').css('margin-left', '340px');
    } else {
        $('#sidebar-button').css('transform', 'none');
        $('.sidebar-plugin').css('display', 'none');
        $('#sidebar-title').css('display', 'none');
        $('#home-sidebar').css('width', '60px');
        $('.dashboard-container').css('margin-left', '60px');
    }
}

$('#sidebar-button').click(function () {
    isExtended = !isExtended;
    processSidebarState();
});


$sidebar.click(function(e) {
    if (!isExtended) {
        if (e.target !== this) return;
        isExtended = true;
        processSidebarState();
    }
});