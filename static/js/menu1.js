function callFunction(buttonFunction) {
    $.ajax({
        type: 'GET',
        url: '/actions/button_click/' + buttonFunction,
        success: function(response) {
            $('#messageLabel').text(response.message);
        },
        error: function(error) {
            console.log(error);
            console.log(buttonFunction)
        }
    });
}