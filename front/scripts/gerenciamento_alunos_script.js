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
    }
    
  }
}

GetAlunos();
