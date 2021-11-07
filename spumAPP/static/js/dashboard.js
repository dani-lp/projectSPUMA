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