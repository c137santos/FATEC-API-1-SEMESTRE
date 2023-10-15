// Função para buscar turmas no servidor
let turmaData;
async function GetTurmas() {
  try {
    const response = await fetch("http://127.0.0.1:8080/api/v1/turmas/get");
    turmaData = await response.json();
    console.log(turmaData);

    // Chama a função para exibir as turmas
    exibirTurmas(turmaData);
  } catch (error) {
    console.error("Erro ao buscar dados da API -> ", error);
    return null;
  }
}

// Função para exibir as turmas no DOM
function exibirTurmas(turmadata) {
  const container = document.querySelector(".flex-warp-container");
  // Itera sobre os objetos do JSON e cria elementos HTML para cada turma
  for (const turmaId in turmadata) {
    if (turmadata.hasOwnProperty(turmaId)) {
      const turma = turmadata[turmaId];

      // Cria um elemento div para representar uma turma
      const turmaSquare = document.createElement("div");
      turmaSquare.className = "turma-square";
      turmaSquare.id = `${turmaId}`; // Adiciona o ID da turma ao turmaSquare

      // Cria elementos de parágrafo para o nome da turma e nome do professor
      const nomeTurma = document.createElement("p");
      nomeTurma.textContent = `Nome da Turma: ${turma.nome}`;

      const nomeProfessor = document.createElement("p");
      nomeProfessor.textContent = `Professor: ${turma.professor}`;

      // Adiciona os parágrafos ao turmaSquare
      turmaSquare.appendChild(nomeTurma);
      turmaSquare.appendChild(nomeProfessor);

      // Cria um ícone de lixeira para deletar a turma
      const imagemIcon = document.createElement("img");
      imagemIcon.src = "../front/icon/trash-icon.svg";
      imagemIcon.alt = "Ícone";
      imagemIcon.className = "trash-icon";
      imagemIcon.id = `${turmaId}`; // Adiciona o ID da turma ao ícone de deletar

      // Adiciona o ícone ao turmaSquare
      turmaSquare.appendChild(imagemIcon);

      // Adiciona o turmaSquare ao container
      container.appendChild(turmaSquare);
    }
  }
}
GetTurmas();