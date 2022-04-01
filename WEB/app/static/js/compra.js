var num_campos = 5;
var inputnum = [];
var insumos = [];
var venta = new Object();
venta.mercancias = [];



function nuevoPro() {
    num = 1 + inputnum.length
    inputnum.push(num)

    //alert("nuevo")
    $("#ListaInsumo").append("<tr>" +
        "<td hidden><input id='txtId" + num + "'  name='Idinsumo[]' type='text' size='15'   required/></td>" +
        "<td><input id='txtIns" + num + "' name='insumo[]'   type='text' size='15' placeholder='Ingresa Marca' required/></td>" +
        "<td><input name='cantinsumo[]' type='Number' size='10'  required/></td>" +
        "<td><input name='precioins[]' type='number' size='10' placeholder='Ingresa precio unitario' required/></td>" +
        "<td><input type='button' value='Eliminar' onclick='eliminar(this)' class='btn btn-danger eliminar'></td>" +
        "</tr>")
    var insumoNombre = $("#txtInsumos  option:selected").text()
    var insumoNum = $("#txtInsumos").val()


    $("#txtId" + num + "").val(insumoNum.trim());
    $("#txtIns" + num + "").val(insumoNombre.trim());
}

function guardar() {


    var res = $("form#f").serializeArray();
    //console.log(res)//descomenta esta linea y mira la consola, así llegan nuestros datos,
    var nprod = res.length;
    var cont = 0;
    $("#result").empty(); //limpiar la caja
    var productos = []; //un array que contendra a los arrays (filas o productos)
    var producto = []; //array para cada una de las filas 
    for (i = 0; i < nprod; i++) { //debe imprimer de 4 en 4 porque estan todos los inputs en un solo array

        $("#result").append(res[i].value);

        //VALIDAR SIEMPRE
        producto.push(res[i].value); //esta linea agrega los datos a nuestro array

        if (cont < 4 - 1) {
            $("#result").append(", ");
            cont++;
        } else {
            $("#result").append(" <br />");
            productos.push(producto);
            producto = [];
            cont = 0;
        }
    }
    console.log(productos); //productos es un array que contiene n arrays (n productos)
    a = JSON.stringify(productos)
    alert(a)
}


function eliminar(e) {
    $(e).parent().parent().fadeOut(400).remove();
    /**
     * el boton eliminar esta jerarquicamente asi:
     *      form > table > tr > td > input.eliminar
     * por esta razon se debe subir dos posiciones 
     */
}