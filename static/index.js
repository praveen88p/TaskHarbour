
document.addEventListener('DOMContentLoaded', function() {
  // Get references to form elements
  var form = document.getElementById('uploadForm');
  var fileInput = document.getElementById('fileInput');
  var uploadButton = document.getElementById('uploadButton');

  // Add event listener to upload button
  uploadButton.addEventListener('click', function() {
    // Check if a file is selected
    if (fileInput.files.length === 0) {
      alert('Please select a file.');
      return;
    }

    // Create FormData object to hold form data
    var formData = new FormData();

    // Append file to FormData object
    formData.append('file', fileInput.files[0]);

    // Send AJAX request to server
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '{% url "image-upscale" %}', true);
    xhr.onload = function() {
      if (xhr.status === 200) {
        // Success
        alert('Image uploaded successfully.');
      } else {
        // Error
        alert('Error uploading image.');
      }
    };
    xhr.send(formData);
  });
});
