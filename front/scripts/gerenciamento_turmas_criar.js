const criarTurmaButton = document.querySelector(".submit-turma");
criarTurmaButton.addEventListener("click", coletaDadosNovaTurma);


async function coletaDadosNovaTurma() {
  const turmaNome = document.getElementById("turmaNome").value;
  const professor = document.getElementById("professor").value;
  const dataInicio = document.getElementById("dataInicio").value;
  const duracaoCiclo = document.getElementById("duracaoCiclo").value;
  console.log(dataInicio);

  const regex = /^[A-Za-zÀ-ÖØ-öø-ÿ\s]*$/;
  if (turmaNome === "") {
    alert("O Nome da Turma é obrigatório.");
    return;
  } else if (!regex.test(turmaNome)) {
    alert("O Nome da Turma deve conter apenas letras e espaços.");
    return;
  }
  if (professor === "") {
    alert("O Professor responsável é obrigatório.");
    return;
  } else if (!regex.test(professor)) {
    alert("O Professor responsável deve conter apenas letras e espaços.");
    return;
  }
  if (dataInicio === "") {
    alert("A Data de início é obrigatório.");
    return;
  }
  if (duracaoCiclo === "") {
    alert("A duração de ciclos, em dias, é obrigatório.");
    return;
  }
  // Formata a data
  const dataInicioForm = moment(dataInicio).format("DD/MM/YYYY");

  const alunos_adicionados = pegarAlunosSelecionados(alunos_todos)

  // Construir o objeto de turma
  const novaTurmaData = {
    nome: turmaNome,
    professor: professor,
    data_de_inicio: dataInicioForm,
    duracao_ciclo: duracaoCiclo,
    quantidade_ciclos: 4,
    alunos_adicionados: alunos_adicionados
  };
  console.log(novaTurmaData);

  criarNovaTurma(novaTurmaData)
  window.location.href = "http://127.0.0.1:5500/front/gerenciamento_turmas.html"
}

//Função para enviar as informações da nova turma em formato de string para o back end
async function criarNovaTurma(novaTurmaData) {
  try {
    const response = await fetch(`http://127.0.0.1:8080/api/v1/turmas/criar`, {
      method: "POST",
      body: JSON.stringify(novaTurmaData),
    });
  } catch (error) {
    console.error("Erro ao enviar os dados para o servidor: " + error);
  }
}

let alunos_todos = listarAlunos()

async function listarAlunos(){
    try {
        const response = await fetch(
        "http://127.0.0.1:8080/api/v1/alunos/listar"
        );
        alunos_todos = await response.json();
        console.log(alunos_todos)
        addAlunosPossiveis(alunos_todos)
        return alunos_todos
    } catch (error) {
        console.error("Erro ao buscar dados da API -> ", error);
        return null;
    }
}

function addAlunosPossiveis(alunos) {
    const divListarAlunos = document.getElementById("listarAlunos");
    for (const aluno in alunos) {
      const divOrganiza = document.createElement("div") 
      divOrganiza.className = "divsNomes" 
      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.name = alunos[aluno].RA;
      checkbox.id = alunos[aluno].RA;
      const label = document.createElement("label");
      label.textContent = alunos[aluno].nome;
      label.htmlFor = alunos[aluno].RA;
      divOrganiza.appendChild(checkbox);
      divOrganiza.appendChild(label);
      divListarAlunos.appendChild(divOrganiza);
    }
  }

  function pegarAlunosSelecionados(alunos) {
    const divListarAlunos = document.getElementById("listarAlunos");
    const alunosArray = Object.values(alunos);
    const alunosSelecionados = [];
    for (const aluno of alunosArray) {
      const checkbox = document.getElementById(aluno.RA);
      if (checkbox.checked) {
        alunosSelecionados.push({
          RA: aluno.RA,
          nome: aluno.nome,
        });
      }
    }
    return alunosSelecionados;
  }
