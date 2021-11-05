let extended = false;

const menuToggle = document.querySelector('.topbar-menu-toggle');
const menuDropdown = document.querySelector('.topbar-menu-collapse');
const menuButtons = document.querySelector('.menu-buttons');

menuToggle.onclick = () => {
    extended = !extended;

    if (extended) {
        menuDropdown.style.height = '100%';
        menuButtons.style.display = 'block';
    } else {
        menuDropdown.style.height = '0';
        menuButtons.style.display = 'none';
    }
}