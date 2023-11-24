var orientacoesBotoes = false;

function inicializaPaginaExportacaoRelatorio() {
    listarTurmas();
}

async function listarTurmas() {
    try {
        const response = await fetch("http://127.0.0.1:8080/api/v1/turmas/listar");
        const turmaData = await response.json();

        const opcoesTurma = document.getElementById("selecionaTurma");

        for (const turmaId in turmaData) {
            if (turmaData.hasOwnProperty(turmaId)) {
                const turma = turmaData[turmaId];
                const option = document.createElement("option");
                option.value = turmaId;
                option.dataset.nome = turma.nome;  // Ajuste para camelCase
                option.textContent = turma.nome;
                opcoesTurma.appendChild(option);
            }
        }
    } catch (error) {
        console.error("Erro ao buscar dados da API -> ", error);
    }
}

async function exportacaoRelatorio(event) {
  event.preventDefault();
  const turmaSelecionada = document.getElementById("selecionaTurma");
  const idTurma = turmaSelecionada.value;

  let relatorioData;

  try {
      relatorioData = await solicitaRelatorio(idTurma);
  } catch (error) {
      console.error('Erro ao exportar relatório:', error);
      return;
  }

  await iniciarDownload(relatorioData);
}


async function solicitaRelatorio(idTurma) {
  try {
      const response = await fetch(`http://127.0.0.1:8080/api/v1/relatorios/${idTurma}`);
      const relatorioData = await response.json();
      return relatorioData;
  } catch (error) {
      console.error("Erro na geração do relatório para download", error);
      throw error
  }
}

async function iniciarDownload(path) {
  try {
    debugger
      let link
      link.href = path;
      const partesDoCaminho = path.split('/')
      const nomeDoArquivo = partesDoCaminho[partesDoCaminho.length - 1]
      link.download = `${nomeDoArquivo}.csv`
      link.click()
  } catch (error) {
      console.error('Erro ao iniciar o download:', error)
  }
}