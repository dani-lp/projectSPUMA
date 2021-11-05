let extended = false;

const menuToggle = document.querySelector('.topbar-menu-toggle');
const menuDropdown = document.querySelector('.topbar-menu-collapse');

menuToggle.onclick = () => {
    extended = !extended;

    if (extended) {
        menuDropdown.style.height = '100%';
    } else {
        menuDropdown.style.height = '0';
    }
}