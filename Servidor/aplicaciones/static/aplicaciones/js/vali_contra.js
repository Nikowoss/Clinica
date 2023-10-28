var password1 = document.getElementById("contraPaciente");
var password2 = document.getElementById("contra2");
var subButton = document.getElementById("subButton");
var error = document.getElementById("error");
var rutPaciente = document.getElementById("rutPaciente");
var erro = document.getElementById("erro");



password1.addEventListener("input",validarContraseñas);
password2.addEventListener("input",validarContraseñas);
rutPaciente.addEventListener("input",Validarrut);


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

function Validarrut() {
    if (validarRUT(rutPaciente)) {
        subButton.disabled = false;
        erro.textContent="es verdad";
    } else {
        subButton.disabled = true;
        erro.textContent = "es falso";
        console.log("El rut no es valido");
    }
}



function validarRUT(rutt) {
    // Eliminar puntos y guión, si los hay
    let rut = rutt.value;
    rut = rut.toString();
    rut = rut.replace(/[.-]/g, "");
    console.log(rut);
    const val = /^\d{1,8}-?[\dkK]{1}$/.test(rut);
    if ( val == true ) {

        const dv = rut.slice(-1); // Dígito verificador
        const num = rut.slice(0, -1); // Número

        let suma = 0;
        let mul = 2;

        for (let i = num.length - 1; i >= 0; i--) {
            suma += parseInt(num[i]) * mul;
            mul = (mul % 7 === 0) ? 2 : mul + 1;
            
        }
        console.log("paso el for");
        const dvEsperado = (11 - (suma % 11)) % 11;
        const dvCalculado = (dv === 'K') ? 10 : parseInt(dv);

        return dvCalculado === dvEsperado;
    }

    return false;
}