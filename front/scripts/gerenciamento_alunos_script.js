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
  const container = document.querySelector(".flex-warp-container");

  for (const alunoId in alunosData) {
    if (alunosData.hasOwnProperty(alunoId)) {
      const aluno = alunosData[alunoId];

      const studentContainer = document.createElement("div");
      studentContainer.className = "student-container";

      const alunoSquare = document.createElement("div");
      alunoSquare.className = "aluno-square";
      alunoSquare.id = `${alunoId}`;

      const nomeAluno = document.createElement("p");
      nomeAluno.className = "aluno";
      nomeAluno.textContent =
        aluno.nome.charAt(0).toUpperCase() + aluno.nome.slice(1);

      alunoSquare.appendChild(nomeAluno);
      container.appendChild(alunoSquare);

      const [grupoNome, turmaNome] = buscaTurmaGrupo(alunoId);
      console.log(grupoNome, turmaNome);
      const turmaElemento = document.createElement("p");
      turmaElemento.className = "turma";
      turmaElemento.textContent =
        turmaNome.charAt(0).toUpperCase() + turmaNome.slice(1);
      alunoSquare.appendChild(turmaElemento);

      const grupoElemento = document.createElement("p");
      grupoElemento.className = "grupo";
      grupoElemento.textContent =
        grupoNome.charAt(0).toUpperCase() + grupoNome.slice(1);
      alunoSquare.appendChild(grupoElemento);

      const acordeaoContent = document.createElement("div");
      acordeaoContent.className = "acordeao-content";
      acordeaoContent.style.display = "none";
      container.appendChild(acordeaoContent);

      // Adicione notas e média ao acordeão
      const notas = notasEmedia[alunoId].notas.join(", ");
      const media = notasEmedia[alunoId].media;

      const notasElemento = document.createElement("p");
      notasElemento.className = "notas";
      notasElemento.textContent = `Notas: ${notas}`;
      acordeaoContent.appendChild(notasElemento);

      const mediaElemento = document.createElement("p");
      mediaElemento.className = "media";
      mediaElemento.textContent = `Média: ${media}`;
      acordeaoContent.appendChild(mediaElemento);

      // Adicione um evento de clique para mostrar/ocultar o acordeão
      alunoSquare.addEventListener("click", () => {
        if (acordeaoContent.style.display === "none") {
          acordeaoContent.style.display = "flex";
        } else {
          acordeaoContent.style.display = "none";
        }
      });
    }
  }
}

const notasEmedia = {
  1: {
    notas: [8, 7, 9],
    media: 8,
  },
  2: {
    notas: [6, 7, 5],
    media: 6,
  },
  3: {
    notas: [9, 8, 8],
    media: 8.3,
  },
};

function buscaTurmaGrupo(alunoId) {
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

  if (alunoId in grupoAluno) {
    const grupoId = grupoAluno[alunoId].grupo;
    if (grupoId in grupos) {
      const grupoNome = grupos[grupoId].nome;
      const turmaId = grupos[grupoId].turma;
      const turma = turmas[turmaId];
      if (turma) {
        return [grupoNome, turma.nome]; // Retorna o nome da turma
      }
    }
  }
  return null;
}

GetAlunos();
