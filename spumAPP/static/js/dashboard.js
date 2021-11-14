const $sbTasks = $('#sidebar-tasks-plugin');
const $sbNotes = $('#sidebar-notes-plugin');

const $dbTasks = $('#tasks-plugin');
const $dbNotes = $('#notes-plugin');

let showTasks = true;
let showNotes = true;

$sbTasks.click(function() {
	showTasks = !showTasks;

	if (showTasks) {
		$sbTasks.css('filter', 'none');
		$dbTasks.css('display', 'block')
	} else {
		$sbTasks.css('filter', 'grayscale(100%)');
		$dbTasks.css('display', 'none')
	}
});

$sbNotes.click(function() {
	showNotes = !showNotes;

	if (showNotes) {
		$sbNotes.css('filter', 'none');
		$dbNotes.css('display', 'block')
	} else {
		$sbNotes.css('filter', 'grayscale(100%)');
		$dbNotes.css('display', 'none')
	}
});

// Dashboards settings menu
$settingsButton = $('#dashboard-settings-button');
$settingsMenu = $('#dashboard-settings-menu');
$settingsMenuContent = $('#dashboard-settings-menu-content');
$editForm = $('#edit-note-form');
$editButton = $('#edit-dashboard-button');
$deleteButton = $('#delete-dashboard-button');
let settingsMenuState = false;

$settingsButton.click(function() {
	settingsMenuState = !settingsMenuState;

	if (settingsMenuState) {
		$settingsMenu.css('height', '370px');
		$settingsMenuContent.css('display', 'flex');
	} else {
		$settingsMenu.css('height', '0');
		$settingsMenuContent.css('display', 'none');
	}
});

$editButton.click(function() {
	$editForm.trigger('reset');
});

$(document).on('click', function (e) {
    if(
        $(e.target).closest($settingsMenu).length == 0 &&
        $(e.target).closest($settingsButton).length == 0 &&
        settingsMenuState
    ) {
        $settingsMenu.css('height', '0');
		$settingsMenuContent.css('display', 'none');
        settingsMenuState = false;
    }
});