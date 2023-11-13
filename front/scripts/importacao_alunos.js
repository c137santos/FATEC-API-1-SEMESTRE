// Função para buscar turmas no servidor

// Função para listar turmas no elemento select
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
        option.textContent = turma.nome;

        opcoesTurma.appendChild(option);
      }
    }
  } catch (error) {
    console.error("Erro ao buscar dados da API -> ", error);
  }
}

function importarArquivo() {
  const aruivoImportado = document.getElementById("arquivo");
  const nomeArquivo = aruivoImportado.files[0].name;
  const turmaSelecionada = document.getElementById("selecionaTurma");
  const nomeTurmaSelecionada =
    turmaSelecionada.options[turmaSelecionada.selectedIndex].dataset.Nome;
  const idTurmaSelecionada = turmaSelecionada.value;

  if (idTurmaSelecionada && nomeArquivo) {
    alert(
      "Turma selecionada: " +
        nomeTurmaSelecionada +
        " " +
        idTurmaSelecionada +
        "\nNome do arquivo: " +
        nomeArquivo
    );
  } else {
    alert("Selecione uma turma e um arquivo.");
  }
}
listarTurmas(); // Chama a função para listar turmas no carregamento da página
