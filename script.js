var login = document.getElementById('login')
var senha = document.getElementById('senha');

form.addEventListener('submit', function(e) {
    // alerta o valor do campo
    alert(login.value);
    alert(senha.value);
     // impede o envio do form
     e.preventDefault();
});