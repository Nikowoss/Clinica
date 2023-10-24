const form = document.getElementById('form');
const rutPacienteInput = document.getElementById('rutPaciente');
const nomPacienteInput = document.getElementById('nomPaciente');
const apePacienteInput = document.getElementById('apePaciente');
const correoInput = document.getElementById('correo');
const contraPacienteInput = document.getElementById('contraPaciente');


const rutPaciente = /^([1-9]{1}|([1-9]{1}[0-9]{1}))\.(\d{3}\.\d{3}-)([a-zA-Z]{1}$|\d{1}$)/;// EL rut comoletio con . y -
const nomPaciente = /^[a-zA-ZÀ-ÿ\s]{3,40}$/; // Letras y espacios, pueden llevar acentos.
const apePaciente = /^[a-zA-ZÀ-ÿ\s]{4,40}$/; // Letras y espacios, pueden llevar acentos.
const correoPaciente = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
const contraPaciente = /^.{4,12}$/; // 4 a 12 digitos.

function validareRut(rut) {
    return rutPaciente.test(rut);
}
function validarNombre(nombre) {
    return nomPaciente.test(nombre);
}
function validarApellido(apellido) {
    return apePaciente.test(apellido);
}
function validarCorreo(correo) {
    return correoPaciente.test(correo);
}
function validarContra(contra) {
    return contraPaciente.test(contra);
}

form.addEventListener('submit', function (event) {
    const rutPaciente = rutPacienteInput.value;
    const nomPaciente = nomPacienteInput.value;
    const apePaciente = apePacienteInput.value;
    const correo = correoInput.value;
    const contraPaciente = contraPacienteInput.value;

    if (!validareRut(rutPaciente)) {
        alert('Rut no válido');
        event.preventDefault();
    }
    if (!validarNombre(nomPaciente)) {
        alert('Nombre no válido');
        event.preventDefault();
    }
    if (!validarApellido(apePaciente)) {
        alert('Apellido no válido');
        event.preventDefault();
    }
    if (!validarCorreo(correo)) {
        alert('Correo no válido');
        event.preventDefault();
    }
    if (!validarContra(contraPaciente)) {
        alert('COntraseña no válido');
        event.preventDefault();
    }
});

rutPacienteInput.addEventListener('input', function () {
    const rut = rutPacienteInput.value;
    
    if (validareRut(rut)) {
        pass
    } else {
        //Mostrar mensaje de error con swal
    }
});
nomPacienteInput.addEventListener('input', function () {
    const nombre = nomPacienteInput.value;
    
    if (validarNombre(nombre)) {
        pass
    } else {
        //Mostrar mensaje de error con swal
    }
});
apePacienteInput.addEventListener('input', function () {
    const apellido = apePacienteInput.value;
    
    if (validarApellido(apellido)) {
        pass
    } else {
        //Mostrar mensaje de error con swal
    }
});
correoInput.addEventListener('input', function () {
    const correo = correoInput.value;
    
    if (validarCorreo(correo)) {
        pass
    } else {
        //Mostrar mensaje de error con swal
    }
});
contraPacienteInput.addEventListener('input', function () {
    const contraPaciente = contraPacienteInput.value;
    
    if (validarContra(contraPaciente)) {
        pass
    } else {
        //Mostrar mensaje de error con swal
    }
});
