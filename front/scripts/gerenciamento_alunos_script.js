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

      const alunoSquare = document.createElement("div");
      alunoSquare.className = "aluno-square";
      alunoSquare.id = `${alunoId}`;

      const nomeAluno = document.createElement("p");
      nomeAluno.textContent = `${aluno.nome}`;

      alunoSquare.appendChild(nomeAluno);
      container.appendChild(alunoSquare);
    }
  }
}

GetAlunos();
