function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

document.addEventListener('DOMContentLoaded', () => {
  const searchInput = document.querySelector('#search-exercise');
  const exerciseSelect = document.querySelector('#exercise-select');
  const exerciseOptions = exerciseSelect.querySelectorAll('option');

  searchInput.addEventListener('input', function() {
    const searchText = this.value.toLowerCase();

    exerciseOptions.forEach(option => {
      const optionText = option.textContent.toLowerCase();
      const optionValue = option.value;

      if (optionText.indexOf(searchText) !== -1) {
        option.style.display = '';
      } else {
        option.style.display = 'none';
      }
    });
  });
});