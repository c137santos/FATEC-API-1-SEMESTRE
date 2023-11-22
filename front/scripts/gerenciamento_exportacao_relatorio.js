var ORIENTACOESBOTOES = false

const botaoExportar = document.getElementById("botaoExportar")

botaoExportar.addEventListener("click", async () => {
  await exportacaoRelatorio()
  event.preventDefault()
})


function inicializaPaginaExportacaoRelatorio(){
    listarTurmas()
}

async function listarTurmas() {
    try {
      const response = await fetch("http://127.0.0.1:8080/api/v1/turmas/listar")
      const turmaData = await response.json()
  
      const opcoesTurma = document.getElementById("selecionaTurma")
  
      for (const turmaId in turmaData) {
        if (turmaData.hasOwnProperty(turmaId)) {
          const turma = turmaData[turmaId]
          const option = document.createElement("option")
          option.value = turmaId
          option.dataset.Nome = turma.nome
          option.textContent = turma.nome
          opcoesTurma.appendChild(option)
        }
      }
    } catch (error) {
      console.error("Erro ao buscar dados da API -> ", error)
    }
}


async function exportacaoRelatorio() { 
  const turmaSelecionada = document.getElementById("selecionaTurma")
  const idTurma = turmaSelecionada.value
  response = await solicitaRelatorio(idTurma)
  event.preventDefault(event)
  disponibilizarDownload()
}

function disponibilizarDownload() {
  const bottaoDownload = document.getElementById("bottaoDownload")
  const botaoExportar = document.getElementById("botaoExportar")
    bottaoDownload.disabled = !ORIENTACOESBOTOES
    botaoExportar.disabled = ORIENTACOESBOTOES
}

async function solicitaRelatorio(idTurma) {
  try {
    const response = await fetch(`http://127.0.0.1:8080/api/v1/relatorios/${idTurma}`)
    return response.status === 200
  } catch (error) {
    console.error("Erro na geração do relatório para download", error)
  }
}