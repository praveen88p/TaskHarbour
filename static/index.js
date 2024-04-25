// function upscale_img() {
//   var formData = new FormData();
//   formData.append('image', $('#id_image')[0].files[0]);

//   $.ajax({
//     type: 'POST',
//     url: '/upsc_img/',
//     data: formData,
//     processData: false,
//     contentType: false,
//     success: function(response) {
//       console.log(response.result);
//     },
//     error: function(error) {
//       console.log(error.responseText);
//     }
//   });
// }