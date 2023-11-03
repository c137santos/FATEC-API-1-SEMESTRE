// Função para buscar turmas no servidor
const criarTurmaButton = document.querySelector(".add-turma-button");
criarTurmaButton.addEventListener("click", levaPaginaEditar);

function levaPaginaEditar(){
  window.location.href = "http://127.0.0.1:5500/front/criar_turma.html";
}

let turmaData;
async function GetTurmas() {
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

async function listar_alunos_turma(id) {
  const response = await fetch (`http://localhost:8080/api/v1/turmas_alunos/listar_alunos_da_turma/${id}`)
  const alunos = await response.json()
  return alunos
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
        requisitar_informacoes_turma(`${turmaId}`)
      );

      // Cria elementos de parágrafo para o nome da turma e nome do professor
      const nomeTurma = document.createElement("p");
      nomeTurma.textContent = `Nome da Turma: ${turma.nome}`;

      const nomeProfessor = document.createElement("p");
      nomeProfessor.textContent = `Professor: ${turma.professor}`;

      const alunos = await listar_alunos_turma(turmaId);
      const quantidadeAlunos = document.createElement("p");
      quantidadeAlunos.textContent = `Alunos: ${alunos ? Object.keys(alunos).length : 0}`;

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
        requisitar_excluir_turma(`${turmaId}`);
      });

      const imagemIconEdit = document.createElement("img");
      imagemIconEdit.src = "../front/icon/edit-icon.svg";
      imagemIconEdit.alt = "Icone";
      imagemIconEdit.className = "edit-icon";
      imagemIconEdit.id = `${turmaId}`;
      imagemIconEdit.addEventListener("click", (event) => {
        event.stopPropagation();
        requisitar_editar_turma(`${turmaId}`);
      });

      // Adiciona o ícone ao turmaSquare
      turmaSquare.appendChild(imagemIcon);

      turmaSquare.appendChild(imagemIconEdit);

      // Adiciona o turmaSquare ao container
      container.appendChild(turmaSquare);
    }
  }
}

function requisitar_excluir_turma(id) {
  if (window.confirm("Atenção! A turma será excluída.\nDeseja prosseguir?")) {
    fetch(`http://localhost:8080/api/v1/turmas/excluir/${id}`, {
      method: "POST",
    }).then(document.getElementById(id).remove());
  }
}

function requisitar_editar_turma(id) {
  window.location.href = "editar_turma.html?id=" + id;
}

function requisitar_informacoes_turma(id) {
  window.location.href = "informacoes_turma.html?id=" + id;
}

GetTurmas();

/*
function redirecionarParaPagina(id) {
  if (id === 'turma') {
      window.location.href = 'gerenciamento_turmas.html';
  } }

  document.getElementById('turma').addEventListener('click', function() {
    redirecionarParaPagina('turma');
});
*/