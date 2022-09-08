$(document).on('ready',Iniciar);
// tabla Alumnos
function Iniciar()
{
    $varFormulario = $('#tablaform');
    $varFormulario.hide();

    $varBotonAg =  $('#btnagregaralum');
    $varBotonAg.on('click',agregar);

    $varBotonLi =  $('#btnListaralum');
    $varBotonLi.on('click',listar);

    //Admin
    $varFormulario1 = $('#tablaforadmin');
    $varFormulario1.hide();

    $varBotonAg1 =  $('#btnagregaradmin');
    $varBotonAg1.on  ('click',agregar1);

    $varBotonLi1 =  $('#btnListaradmin');
    $varBotonLi1.on('click',listar1);

    // Promedio 

    $varBotonProm =  $('#btnPromedio');
    $varBotonProm.on  ('click',promedio);

}

function agregar ()
{    
  
    $varTablaalumn1 = $('#tablaalumn')
    $varTablaalumn1.hide();
    $varFormulario = $('#tablaform')
    $varFormulario.show();
}

function listar ()
{
    $varTablaalumn1 = $('#tablaalumn')
    $varTablaalumn1.show();
    $varFormulario = $('#tablaform')
    $varFormulario.hide();


}

var Datos =function(){
    var nombre =document.getElementById("nombre").value;
    var apellido =document.getElementById("apellido").value;
    var carne =document.getElementById("carne").value;
    var nota1 =document.getElementById("nota1").value;
     
   $('#tablaalumn').append('<tr class="child"><td>'+nombre+'</td><td>'+apellido+'</td><td>'+carne+'</td><td>'+nota1+'</td></tr>' );   

   $varTablaalumn1 = $('#tablaalumn')
   $varTablaalumn1.show();

   $varFormulario = $('#tablaform');
    $varFormulario.hide();
}

//Tabla Administradores
function agregar1 (){    
  
    $varTablaadmin = $('#tablaadmin')
    $varTablaadmin.hide();
    $varFormulario2 = $('#tablaforadmin')
    $varFormulario2.show();

}

function listar1 (){
    $varTablaadmin = $('#tablaadmin')
    $varTablaadmin.show();
    $varFormulario2 = $('#tablaforadmin')
    $varFormulario2.hide();

}

var Datos1 =function(){
    var nombre1 =document.getElementById("nombre1").value;
    var apellido1 =document.getElementById("apellido1").value;
    var carne1 =document.getElementById("carne1").value;
    $('#tablaadmin').append('<tr class="child"><td>'+nombre1+'</td><td>'+apellido1+'</td><td>'+carne1+'</td> </tr>' );   
  
    $varFormulario1 = $('#tablaforadmin');
    $varFormulario1.hide();

    $varTablaadmin = $('#tablaadmin')
    $varTablaadmin.show();
}

function promedio() {
     // you can change the values of array
   let array = [70, 95, 52, 95,41]
   let i = 0
   let sum = 0
   let len = array.length;
   let result = 0
    
    // loop for calculate sum of array values
    while (i < len) {
        sum = sum + array[i++];
    }
      result = sum / len
    // simply shows the result in alert box
    alert("Average of ("+array+") is :  "+result);
    alert("3 Aprobados, 2 Reprobados")
}
