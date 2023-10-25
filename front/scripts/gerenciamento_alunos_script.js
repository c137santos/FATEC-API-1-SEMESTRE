let alunosData;
async function GetAlunos() {
  try {
    const response = await fetch("http://127.0.0.1:8080/api/v1/alunos/listar");
    alunosData = await response.json();
    console.log(alunosData);
    exibirAlunos(alunosData);
  } catch (error) {
    console.error("Erro ao buscar dados da API -> ", error);
  }
}

function exibirAlunos(alunosData) {
  const container = document.querySelector(".corpo_tabela");

  for (const alunoId in alunosData) {
    if (alunosData.hasOwnProperty(alunoId)) {
      const aluno = alunosData[alunoId];
      const RAaluno = alunosData[alunoId].RA;

      const alunoSquare = document.createElement("div");
      alunoSquare.className = "aluno-square";
      alunoSquare.id = `${alunoId}`;

      const nomeAluno = document.createElement("p");
      nomeAluno.className = "aluno";
      nomeAluno.textContent =
        aluno.nome.charAt(0).toUpperCase() + aluno.nome.slice(1);

      const alunoRA = document.createElement("p");
      alunoRA.className = "alunoRA";
      alunoRA.textContent = `${RAaluno}`;

      const [grupoNome, turmaNome] = buscaTurmaGrupo(alunoId);
      console.log(grupoNome, turmaNome);

      const editar_excluir_alunos = document.createElement("div");
      editar_excluir_alunos.className = "botoes_editar_excluir_alunos";
      const editarAluno = document.createElement("img");
      editarAluno.src = "../front/icon/edit-icon.svg";
      editarAluno.alt = "Icone";
      editarAluno.className = "edit-icon";
      editar_excluir_alunos.appendChild(editarAluno);
      editarAluno.id = `${alunoId}`;

      // Cria um ícone de lixeira para deletar a turma
      const excluirAluno = document.createElement("img");
      excluirAluno.src = "../front/icon/trash-icon.svg";
      excluirAluno.alt = "Ícone";
      excluirAluno.className = "trash-icon";
      editar_excluir_alunos.appendChild(excluirAluno);
      excluirAluno.id = `${alunoId}`; // Adiciona o ID da turma ao ícone de deletar

      alunoSquare.appendChild(nomeAluno);
      alunoSquare.appendChild(alunoRA);
      alunoSquare.appendChild(editar_excluir_alunos);
      container.appendChild(alunoSquare);
    }
  }
}

function buscaTurmaGrupo(alunoId) {
  const grupoAluno = {
    1: {
      // id aluno
      grupo: 1, // id grupo
    },
    2: {
      grupo: 2,
    },
    3: {
      grupo: 2,
    },
  };

  const grupos = {
    1: {
      // id grupo
      turma: 1, //id turma
      nome: "team bee",
    },
    2: {
      turma: 2,
      nome: "team tatata",
    },
    3: {
      turma: 1,
      nome: "team barbuleta",
    },
  };
  const turmas = {
    1: {
      // id turma
      nome: "ADS",
      professor: "Nadalete",
      data_de_inicio: "21/02/2023",
    },
    2: {
      nome: "Banco de dados",
      professor: "Professora teste",
      data_de_inicio: "2023-10-11",
    },
    3: {
      nome: "Inteligencia Artifical",
      professor: "Grugru",
      data_de_inicio: "16/10/2023",
    },
  };

  if (alunoId in grupoAluno) {
    const grupoId = grupoAluno[alunoId].grupo;
    if (grupoId in grupos) {
      const grupoNome = grupos[grupoId].nome;
      const turmaId = grupos[grupoId].turma;
      const turmaNome = turmas[turmaId].nome;
      return [grupoNome, turmaNome];
    }
  }
}

GetAlunos();
