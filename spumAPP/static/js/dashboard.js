const $sbTasks = $('#sidebar-tasks-plugin');
const $sbNotes = $('#sidebar-notes-plugin');
const $sbHabits = $('#sidebar-habits-plugin');

const $dbTasks = $('#tasks-plugin');
const $dbNotes = $('#notes-plugin');
const $dbHabits = $('#habits-plugin');

let showTasks = true;
let showNotes = true;
let showHabits = true;

$sbTasks.click(function () {
	showTasks = !showTasks;

	if (showTasks) {
		$sbTasks.css('filter', 'none');
		$dbTasks.css('display', 'block')
	} else {
		$sbTasks.css('filter', 'grayscale(100%)');
		$dbTasks.css('display', 'none')
	}
});

$sbNotes.click(function () {
	showNotes = !showNotes;

	if (showNotes) {
		$sbNotes.css('filter', 'none');
		$dbNotes.css('display', 'block')
	} else {
		$sbNotes.css('filter', 'grayscale(100%)');
		$dbNotes.css('display', 'none')
	}
});

$sbHabits.click(function () {
	showHabits = !showHabits;

	if (showHabits) {
		$sbHabits.css('filter', 'none');
		$dbHabits.css('display', 'block')
	} else {
		$sbHabits.css('filter', 'grayscale(100%)');
		$dbHabits.css('display', 'none')
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

$settingsButton.click(function () {
	settingsMenuState = !settingsMenuState;

	if (settingsMenuState) {
		$settingsMenu.css('height', '370px');
		$settingsMenuContent.css('display', 'flex');
	} else {
		$settingsMenu.css('height', '0');
		$settingsMenuContent.css('display', 'none');
	}
});

$editButton.click(function () {
	$editForm.trigger('reset');
});

$(document).on('click', function (e) {
	if (
		$(e.target).closest($settingsMenu).length == 0 &&
		$(e.target).closest($settingsButton).length == 0 &&
		settingsMenuState
	) {
		$settingsMenu.css('height', '0');
		$settingsMenuContent.css('display', 'none');
		settingsMenuState = false;
	}
});

$deleteButton.click(function () {
	const dashboard_id = $(location).attr('href').substring($(location).attr('href').lastIndexOf('/') + 1);
	if (parseInt(dashboard_list_lenght) > 1) {
		if (confirm("Do you want to delete the workspace?")) {
			$.ajax({
				type: 'POST',
				url: dashboard_delete_url,
				data: {
					'dashboard_id': dashboard_id
				},
				success: function (data) {
					window.location.replace(index_url);
				}
			});
		}
	} else {
		alert('This is your only dashboard');
	}
});