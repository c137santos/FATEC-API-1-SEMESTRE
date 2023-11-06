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

    const ciclosData = {};
    for (const turmaId in turmaData) {
      if (turmaData.hasOwnProperty(turmaId)) {
        const responseCiclos = await fetch(
          `http://127.0.0.1:8080/api/v1/ciclos_detalhes/listar/turma/${turmaId}`
        );
        const ciclosInfo = await responseCiclos.json();
        // Modelo do ciclosInfo para uma turma com ciclo 1 aberto, se nao tiver vem como null
        // {"data_final_ciclo": "2023-11-04 00:00:00", "ciclo_atual": 2, "ciclo_aberto_para_nota": 1}
        ciclosData[turmaId] = ciclosInfo;
        console.log(ciclosInfo);
      }
    }

    exibirTurmas(turmaData, ciclosData);
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

function formatarData(data) {
  return new Date(data).toLocaleDateString("pt-BR");
}

// Função para exibir as turmas no DOM
async function exibirTurmas(turmadata, ciclosData) {
  const container = document.querySelector(".flex-warp-container");
  // Itera sobre os objetos do JSON e cria elementos HTML para cada turma
  for (const turmaId in turmadata) {
    if (turmadata.hasOwnProperty(turmaId)) {
      const turma = turmadata[turmaId];
      const ciclosInfo = ciclosData[turmaId]; // Dados dos ciclos para a turma atual

      // Cria um elemento div para representar uma turma
      const turmaSquare = document.createElement("div");
      turmaSquare.className = "turma-square";
      turmaSquare.id = `${turmaId}`; // Adiciona o ID da turma ao turmaSquare
      turmaSquare.addEventListener("click", () =>
        encarminharParaPgInformacoesDaTurma(`${turmaId}`)
      );

      // Cria elementos de parágrafo para o nome da turma e nome do professor
      const nomeTurma = document.createElement("p");
      nomeTurma.textContent = `Turma: ${turma.nome}`;

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
      turmaSquare.appendChild(dataInicioTurma);

      // Adicione as informações dos ciclos
      if (ciclosInfo) {
        // para cada turma retorna um objeto:
        // ciclo_aberto_para_nota vem vazio ou com o numero do ciclo
        // {"data_final_ciclo": "2023-11-04 00:00:00", "ciclo_atual": 2, "ciclo_aberto_para_nota": null}
        const cicloAtual = ciclosInfo.ciclo_atual;
        const dataFinalCiclo = ciclosInfo.data_final_ciclo;
        const cicloAbertoParaNota = ciclosInfo.ciclo_aberto_para_nota;

        const cicloInfoParagrafo = document.createElement("p");
        cicloInfoParagrafo.textContent = `Ciclo Atual: ${cicloAtual}`;
        turmaSquare.appendChild(cicloInfoParagrafo);

        const dataFinalCicloParagrafo = document.createElement("p");
        dataFinalCicloParagrafo.textContent = `Data Final do Ciclo: ${formatarData(
          dataFinalCiclo
        )}`;
        turmaSquare.appendChild(dataFinalCicloParagrafo);

        turmaSquare.appendChild(quantidadeAlunos);

        if (cicloAbertoParaNota) {
          const cicloAbertoNotaParagrafo = document.createElement("p");
          cicloAbertoNotaParagrafo.textContent = `Ciclo aberto: ${cicloAbertoParaNota}`;
          turmaSquare.appendChild(cicloAbertoNotaParagrafo);
        }
      }

      // Cria um ícone de lixeira para deletar a turma
      const imagemIcon = document.createElement("img");
      imagemIcon.src = "../front/icon/trash-icon.svg";
      imagemIcon.alt = "Ícone";
      imagemIcon.className = "trash-icon";
      imagemIcon.id = `${turmaId}`; // Adiciona o ID da turma ao ícone de deletar
      imagemIcon.addEventListener("click", (event) => {
        event.stopPropagation();
        excluirTurma(`${turmaId}`);
      })

      const imagemIconEdit = document.createElement("img");
      imagemIconEdit.src = "../front/icon/edit-icon.svg";
      imagemIconEdit.alt = "Icone";
      imagemIconEdit.className = "edit-icon";
      imagemIconEdit.id = `${turmaId}`;
      imagemIconEdit.addEventListener("click", (event) => {
        event.stopPropagation();
        encaminharParaPaginaEditarTurma(`${turmaId}`);
      })

      // Adiciona o ícone ao turmaSquare
      turmaSquare.appendChild(imagemIcon);

      turmaSquare.appendChild(imagemIconEdit);

      // Adiciona o turmaSquare ao container
      container.appendChild(turmaSquare);
    }
  }
}

async function excluirTurma(turmaId) {
  const confirmed = window.confirm("Atenção! A turma será excluída.\nDeseja prosseguir?")
  if (confirmed) {
    try {
      const response = await fetch(`http://localhost:8080/api/v1/turmas/excluir/${turmaId}`)
      const data = await response.json()
      if (!response.ok) {
        throw new Error(data.mensagem)
      }
    } catch (error) {
      alert(`Houve um problema! ${error.message}`)
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
