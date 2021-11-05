let extended = false;

const menuToggle = document.querySelector('.topbar-menu-toggle');
const menuDropdown = document.querySelector('.topbar-menu-collapse');
const menuContainer = document.querySelector('.topbar-collapse-container');

const processTopbarState = () => {
    if (extended) {
        menuDropdown.style.height = '100%';
        menuContainer.style.opacity = '1';
        menuContainer.style.display = 'flex';
    } else {
        menuDropdown.style.height = '0';
        menuContainer.style.opacity = '0';
        menuContainer.style.display = 'none';
    }
}

menuToggle.onclick = () => {
    extended = !extended;
    processTopbarState();
}

$('.topbar-anchor').click(function() {
    extended = false;
    processTopbarState();
});