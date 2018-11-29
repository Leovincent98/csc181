function login() {
     $.ajax(
         {
             url: "http://127.0.0.1:5000/login/",
             contentType: 'application/json; charset=utf-8',
             data: JSON.stringify({
                 'username': $("#username").val(),
                 'password': $("#password").val()
             }),
             type: "POST",
             dataType: "json",

             error: function (resp) {
                 //window.location.replace('404.html');
             },

             success: function (resp) {
                 if (resp.status === 'ok') {
                     window.location.replace('front.html')
                 }
                 else {
                     window.location.replace('ui/404.html?username=' + resp.message + '/')
                 }
             }
         }
     );

 }