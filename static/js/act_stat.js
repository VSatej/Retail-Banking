function show(val)
{
    if(val==1){
        document.getElementById('no_transt').style.display = 'block';
        document.getElementById('s_date').style.display = 'none';
    }
    else{
        document.getElementById('s_date').style.display = 'block';
        document.getElementById('no_transt').style.display = 'none';
    }
    return;
}

$(document).ready(function() {
    $('.act_state_table').DataTable({
    	searching : false,
        paging: true,
        pageLength: 50,
        lengthChange: false
    });
});

function Export() {
html2canvas(document.getElementById('acc_table'), {
    onrendered: function (canvas) {
        var data = canvas.toDataURL();
        var docDefinition = {
            content: [{
                image: data,
                width: 500
            }]
        };
        pdfMake.createPdf(docDefinition).download("Table.pdf");
    }
});
}

$(function () {
    $("#to_excel").click(function () {
        $("#acc_table").table2excel({
            filename : "account Statement"
        });
    });
});