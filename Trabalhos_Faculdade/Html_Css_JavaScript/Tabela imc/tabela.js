function myFunction() {
    var table = document.getElementById("tabela");
    var row = table.insertRow();
    var nomeCell = row.insertCell(0);
    var notaCell = row.insertCell(1);
    var statusCell = row.insertCell(2);
    nomeCell.innerHTML = "ALUNO-TESTE";
    notaCell.innerHTML = 10;
    statusCell.innerHTML = "APROVADO";
}