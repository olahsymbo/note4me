// Form reference
const form = {}
form.noteTitle = document.querySelector('#titleNoteText');
form.noteText = document.querySelector('#formNoteText');
form.addButton = document.querySelector('#formAddButton');
form.color = document.querySelector('#formColor');

const notes = document.querySelector('#notes');

form.noteTitle.focus();
form.noteText.focus();

// Functions
function addNote() {
  let title = form.noteTitle.value;
  let text = form.noteText.value;
  let note = document.createElement('div');
  let deleteButton = document.createElement('span');

  note.classList.add('note');
  note.classList.add(form.color.value);
  note.innerHTML = `<div class='note-title'>${title}</div>`;
  note.innerHTML = `<div class='note-text'>${text}</div>`;
  deleteButton.classList.add('note-delete');
  deleteButton.innerHTML = '&times;';

  note.appendChild(deleteButton);
  notes.appendChild(note);

  form.noteTitle.value = '';
  form.noteText.value = '';
  form.noteTitle.focus();
  form.noteText.focus();

  addListenerDeleteButton(deleteButton);
}

function addListenerDeleteButton(deleteButton) {
  deleteButton.addEventListener('click', function (e) {
    e.stopPropagation();
    deleteNote(e);
  });
}

function deleteNote(e) {
  let eventNote = e.target.parentNode;
  eventNote.parentNode.removeChild(eventNote);
}

// Event Listeners
form.addButton.addEventListener('click', function (e) {
  e.preventDefault();
  if ((form.noteTitle.value != '') && (form.noteText.value != '')) {
    addNote();
  }
})
