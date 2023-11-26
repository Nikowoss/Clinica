const form = document.getElementById('form');
const correo = document.getElementById('correo');
const contra = document.getElementById('contraPaciente');

form.addEventListener('submit', e=> {
    e.preventDefault();

    if(correo==""||contra==""){
        swal("Ingresa algo en el campo de texto :D")
    }
    else{ 
        
    }
})