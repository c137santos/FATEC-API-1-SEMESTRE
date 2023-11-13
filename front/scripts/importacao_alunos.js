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
        option.dataset.Nome = turma.nome;
        option.textContent = turma.nome;

        opcoesTurma.appendChild(option);
      }
    }
  } catch (error) {
    console.error("Erro ao buscar dados da API -> ", error);
  }
}

function importarArquivo() {
  const arquivoImportado = document.getElementById("arquivo");
  const nomeArquivo = arquivoImportado.files[0].name;
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
    const formData = new FormData();
    formData.append("turma_id", idTurmaSelecionada);
    formData.append("nome_turma", nomeTurmaSelecionada);
    formData.append("nome_arquivo", nomeArquivo);
    formData.append("arquivo", arquivoImportado.files[0]);

    console.log(formData);
    respostaUpload = salvarArquivo(formData);
  } else {
    alert("Selecione uma turma e um arquivo.");
  }
}

async function salvarArquivo(formData) {
  try {
    const response = await fetch(
      "http://127.0.0.1:8080/api/v1/importacao/salvar_arquivo",
      { method: "POST", body: formData }
    );
  } catch (error) {
    console.error("Erro ao buscar dados da API -> ", error);
    return null;
  }
}
