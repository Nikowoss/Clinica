var password1 = document.getElementById("contraPaciente");
var password2 = document.getElementById("contra2");
var subButton = document.getElementById("subButton");
var error = document.getElementById("error")

password1.addEventListener("input",validarContraseñas);
password2.addEventListener("input",validarContraseñas);

function validarContraseñas() {
    var valor1 = password1.value;
    var valor2 = password2.value;

    if (valor1 === valor2) {
        subButton.disabled = false;
        error.textContent="";
    } else {
        subButton.disabled = true;
        error.textContent = "Las contraseñas no coinciden";
    }
}
