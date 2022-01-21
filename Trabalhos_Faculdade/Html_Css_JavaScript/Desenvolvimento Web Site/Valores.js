let btnAprovados = document.querySelector("#btnPainel2")

let btnReprovados = document.querySelector("#btnPainel3")

let btnSalvar = document.querySelector("#btnSalvar")

const salvar = document.getElementById("ExibirPainel1")

const salvar1 = document.getElementById("ExibirPainel2")

const ShowNota1 = document.getElementById("btnSalvar")

let campos = document.querySelectorAll("#ExibirPainel1 input")

btnSalvar.addEventListener("click", () =>{

    console.log(campos)
    console.log(campos.item(0).value)
    console.log(campos.item(1).value)

    let aluno = {
        nome: campos.item(0).value,
        nota: campos.item(1).value
    }

    campos.forEach((cp) =>{
        cp.value=""
    })

    addNovoRegistro(aluno)
    salvar.style.display="none"
    salvar1.style.display="block"

})

function addNovoRegistro(aluno) {
    const MEDIA = 6
    const aprovado = aluno.nota >= MEDIA
    let tabela = document.getElementById(aprovado ? "tabela" : "tabela1")
    let row = tabela.insertRow();
    let nomeCell = row.insertCell(0);
    let notaCell = row.insertCell(1);
    let statusCell = row.insertCell(2);
    nomeCell.innerHTML = `${aluno.nome}`;
    notaCell.innerHTML = `${aluno.nota}`;
    statusCell.innerHTML = aprovado ? "Aprovado" : "Reprovado"
}
