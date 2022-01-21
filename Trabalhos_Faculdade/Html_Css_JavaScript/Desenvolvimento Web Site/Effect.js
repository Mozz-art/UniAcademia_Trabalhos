const home = document.getElementById("HidePainel")

const cadastrar = document.getElementById("btnPainel1")

const cadastrar1 = document.getElementById("ExibirPainel1")

const aprovados = document.getElementById("btnPainel2")

const aprovados1 = document.getElementById("ExibirPainel2")

const reprovados = document.getElementById("btnPainel3")

const reprovados1 = document.getElementById("painelReprovados")









home.addEventListener("click", () => {
    
    cadastrar1.style.display = "none"
    aprovados1.style.display = "none"
    reprovados1.style.display = "none"
    
});

cadastrar.addEventListener("click", () => {
    
    cadastrar1.style.display = "block"
    aprovados1.style.display = "none"
    reprovados1.style.display = "none"
});

aprovados.addEventListener("click", () => {
    
    aprovados1.style.display = "block"
    cadastrar1.style.display = "none"
    reprovados1.style.display = "none"
});

reprovados.addEventListener("click", () => {
    
    reprovados1.style.display = "block"
    cadastrar1.style.display = "none"
    aprovados1.style.display = "none"

});

const subHome = document.getElementById("subHome")

const subCadastrar = document.getElementById("subCadastrar")

const subCadastrar1 = document.getElementById("ExibirPainel1")

const subAprovados = document.getElementById("subAprovados")

const subAprovados1 = document.getElementById("ExibirPainel2")

const subReprovados = document.getElementById("subReprovados")

const subReprovados1 = document.getElementById("painelReprovados")


subHome.addEventListener("click", () => {
    
    subCadastrar1.style.display = "none"
    subAprovados1.style.display = "none"
    subReprovados1.style.display = "none"
    
});

subCadastrar.addEventListener("click", () => {
    
    subCadastrar1.style.display = "block"
    subAprovados1.style.display = "none"
    subReprovados1.style.display = "none"
});

subAprovados.addEventListener("click", () => {
    
    subAprovados1.style.display = "block"
    subCadastrar1.style.display = "none"
    subReprovados1.style.display = "none"
});

subReprovados.addEventListener("click", () => {
    
    subReprovados1.style.display = "block"
    subCadastrar1.style.display = "none"
    subAprovados1.style.display = "none"

});
