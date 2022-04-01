var inputnum = [];

function nuevoPro() {
    num = 1 + inputnum.length
    inputnum.push(num)

    //alert("nuevo")
    $("#ListaInsumo").append("<tr>" +
        "<td hidden><input id='txtId" + num + "' name='Idinsumo" + num + "' type='text' size='15' disabled hidden  required/></td>" +
        "<td><input id='txtIns" + num + "' name='insumo" + num + "'  disabled type='text' size='15' placeholder='Ingresa Marca' required/></td>" +
        "<td><input name='cantinsumo" + num + "' type='Number' size='10'  required/></td>" +
        "<td><input name='precioins" + num + "' type='number' size='10' placeholder='Ingresa precio unitario' required/></td>" +
        "<td><input type='button' value='Eliminar' onclick='eliminar(this)' class='btn btn-danger eliminar'></td>" +
        "</tr>")
    var insumoNombre = $("#txtInsumos  option:selected").text()
    var insumoNum = $("#txtInsumos").val()


    $("#txtId" + num + "").val(insumoNum.trim());
    $("#txtIns" + num + "").val(insumoNombre.trim());

    ins = $("#txtId" + num + "").val();
}