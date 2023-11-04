// Função para buscar turmas no servidor
const criarTurmaButton = document.querySelector(".add-turma-button");
criarTurmaButton.addEventListener("click", levaPaginaEditar);

function levaPaginaEditar() {
  window.location.href = "http://127.0.0.1:5500/front/criar_turma.html";
}

let turmaData;
async function getTurmas() {
  try {
    const response = await fetch("http://127.0.0.1:8080/api/v1/turmas/listar");
    turmaData = await response.json();
    console.log(turmaData);

    // Chama a função para exibir as turmas
    await exibirTurmas(turmaData);
  } catch (error) {
    console.error("Erro ao buscar dados da API -> ", error);
    return null;
  }
}

async function listarAlunosTurma(id) {
  const response = await fetch(
    `http://localhost:8080/api/v1/turmas_alunos/listar_alunos_da_turma/${id}`
  );
  const alunos = await response.json();
  return alunos;
}

// Função para exibir as turmas no DOM
async function exibirTurmas(turmadata) {
  const container = document.querySelector(".flex-warp-container");
  // Itera sobre os objetos do JSON e cria elementos HTML para cada turma
  for (const turmaId in turmadata) {
    if (turmadata.hasOwnProperty(turmaId)) {
      const turma = turmadata[turmaId];

      // Cria um elemento div para representar uma turma
      const turmaSquare = document.createElement("div");
      turmaSquare.className = "turma-square";
      turmaSquare.id = `${turmaId}`; // Adiciona o ID da turma ao turmaSquare
      turmaSquare.addEventListener("click", () =>
        encarminharParaPgInformacoesDaTurma(`${turmaId}`)
      );

      // Cria elementos de parágrafo para o nome da turma e nome do professor
      const nomeTurma = document.createElement("p");
      nomeTurma.textContent = `Nome da Turma: ${turma.nome}`;

      const nomeProfessor = document.createElement("p");
      nomeProfessor.textContent = `Professor: ${turma.professor}`;

      const alunos = await listarAlunosTurma(turmaId);
      const quantidadeAlunos = document.createElement("p");
      quantidadeAlunos.textContent = `Alunos: ${
        alunos ? Object.keys(alunos).length : 0
      }`;

      const dataInicioTurma = document.createElement("p");
      dataInicioTurma.textContent = `Data de Início: ${turma.data_de_inicio}`;

      // Adiciona os parágrafos ao turmaSquare
      turmaSquare.appendChild(nomeTurma);
      turmaSquare.appendChild(nomeProfessor);
      turmaSquare.appendChild(quantidadeAlunos);
      turmaSquare.appendChild(dataInicioTurma);

      // Cria um ícone de lixeira para deletar a turma
      const imagemIcon = document.createElement("img");
      imagemIcon.src = "../front/icon/trash-icon.svg";
      imagemIcon.alt = "Ícone";
      imagemIcon.className = "trash-icon";
      imagemIcon.id = `${turmaId}`; // Adiciona o ID da turma ao ícone de deletar
      imagemIcon.addEventListener("click", (event) => {
        event.stopPropagation();
        excluirTurma(`${turmaId}`);
      });

      const imagemIconEdit = document.createElement("img");
      imagemIconEdit.src = "../front/icon/edit-icon.svg";
      imagemIconEdit.alt = "Icone";
      imagemIconEdit.className = "edit-icon";
      imagemIconEdit.id = `${turmaId}`;
      imagemIconEdit.addEventListener("click", (event) => {
        event.stopPropagation();
        encaminharParaPaginaEditarTurma(`${turmaId}`);
      });

      // Adiciona o ícone ao turmaSquare
      turmaSquare.appendChild(imagemIcon);

      turmaSquare.appendChild(imagemIconEdit);

      // Adiciona o turmaSquare ao container
      container.appendChild(turmaSquare);
    }
  }
}

async function excluirTurma(id) {
  const confirmed = window.confirm("Atenção! A turma será excluída.\nDeseja prosseguir?");
  if (confirmed) {
    try {
      const response = await fetch(`http://localhost:8080/api/v1/turmas/excluir/${id}`, {
        method: "POST",
      });
      if (!response.ok) {
        throw new Error('Erro ao excluir a turma.');
      }
      document.getElementById(id).remove();
    } catch (error) {
      console.error('Houve um problema ao excluir a turma:', error.message);
    }
  }
}

function encaminharParaPaginaEditarTurma(id) {
  window.location.href = "editar_turma.html?id=" + id;
}

function encarminharParaPgInformacoesDaTurma(id) {
  window.location.href = "informacoes_turma.html?id=" + id;
}

getTurmas();
