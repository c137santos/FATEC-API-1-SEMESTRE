// Função para buscar turmas no servidor



// Função para listar turmas no elemento select
async function listarTurmas() {
  try {
    const response = await fetch("http://127.0.0.1:8080/api/v1/turmas/listar");
    const turmaData = await response.json();

    const Turmas = document.getElementById("fnome");

    for (const turmaId in turmaData) {
      if (turmaData.hasOwnProperty(turmaId)) {
        const turma = turmaData[turmaId];

        const option = document.createElement("option");
        option.value = turmaId;
        option.textContent = turma.nome;

        Turmas.appendChild(option);
      }
    }
  } catch (error) {
    console.error("Erro ao buscar dados da API -> ", error);
  }
}

listarTurmas(); // Chama a função para listar turmas no carregamento da página
