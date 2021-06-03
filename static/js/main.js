
  const SERVER_URL = 'localhost'
  
  
  var colorPicker = new iro.ColorPicker("#color_picker", {
    // Set the size of the color picker
    width: 320,
    // Set the initial color to pure red
    color: "#34a4eb"
  });

  function getColor() {
      
    var color_test = document.querySelector('.color_test');

    let picked_color = colorPicker.color.hexString;

    let json_color = {
      'color' : picked_color,
    }

    $.ajax({
      type: 'POST',
      url: "/lights",
      contentType: 'application/json',
      data: JSON.stringify(json_color) ,
      success: function (result) {

        console.log(result + 'ok');
        color_test.style.backgroundColor = colorPicker.color.hexString;

      },
      error: function (error) {
        console.log(error);
      }
    });

    

  }
