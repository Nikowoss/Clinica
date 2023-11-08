document.getElementById("form").addEventListener("submit", function(event) {
    const fecha_str = document.getElementById("fechainicio").value;;  // Ejemplo de cadena de fecha en formato "dd/mm/yyyy"
    const partes = fecha_str.split('-'); // Divide la cadena en partes usando el caracter '/'
    const dia = partes[0];
    const mes = partes[1] - 1; // Resta 1 al mes ya que en JavaScript los meses se indexan desde 0 (enero = 0)
    const año = partes[2];
    
    const fecha_obj = new Date(año, mes, dia);
    
    console.log(fecha_obj);
  });
  
