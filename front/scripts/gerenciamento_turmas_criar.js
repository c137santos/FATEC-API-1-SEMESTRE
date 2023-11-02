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

  // Formata a data para dia/mes/ano

  const data = new Date(dataInicio);
  const dia = String(data.getDate()).padStart(2, "0"); // Garante que o dia tenha sempre 2 dígitos
  const mes = String(data.getMonth() + 1).padStart(2, "0"); // Garante que o mês tenha sempre 2 dígitos
  const ano = data.getFullYear();
  // const dataFormatada = `${dia}/${mes}/${ano}`;

  if (ano < 1000 || ano > 9999) {
    alert("O ano deve ter exatamente 4 dígitos.");
    return;
  }

  const dataFormatada = dataInicio.split("-").reverse().join("/");
  const alunos_adicionados = pegarAlunosSelecionados(alunos_todos)

  // Construir o objeto de turma
  const novaTurmaData = {
    nome: turmaNome,
    professor: professor,
    data_de_inicio: dataFormatada,
    duracao_ciclo: duracaoCiclo,
    quantidade_ciclos: 4,
    alunos_adicionados: alunos_adicionados
  };
  console.log(novaTurmaData);

  // Exiba a div de confirmação
  const confirmacaoContainer = document.getElementById("confirmacaoContainer");
  confirmacaoContainer.style.display = "block";

  // Preencha os detalhes da turma na div de confirmação
  document.getElementById("turmaNomeConfirmacao").textContent = turmaNome;
  document.getElementById("professorConfirmacao").textContent = professor;
  document.getElementById("dataInicioConfirmacao").textContent = dataFormatada;
  document.getElementById("duracaoCicloConfirmacao").textContent = duracaoCiclo;

  //aciona evento para enviar os dados da turma que sera criada para o back end
  const confirmarButton = document.getElementById("confirmarButton");
  confirmarButton.addEventListener("click", function (event) {
    event.preventDefault();
    console.log(novaTurmaData);
    criarNovaTurma(novaTurmaData);
  });
}

// Fechar modal de confirmação de criação
function closeConfirmacao() {
  const confirmacaoContainer = document.getElementById("confirmacaoContainer");
  confirmacaoContainer.style.display = "none";
}

//Função para enviar as informações da nova turma em formato de string para o back end
async function criarNovaTurma(novaTurmaData) {
  try {
    const response = await fetch(`http://127.0.0.1:8080/api/v1/turmas/criar`, {
      method: "POST",
      body: JSON.stringify(novaTurmaData),
    });

    // Verifica se a resposta da solicitação está OK (status 200)
    if (response.ok) {
      const resposta = await response.json();
      const mensagem = resposta.mensagem;
      const detalhes = resposta.detalhes;
      alert("Resposta do servidor:\n" + mensagem + "\n" + detalhes.join("\n"));
      window.location.href = "gerenciamento_turmas.html";
    } else {
      // Lida com erros de resposta, se houver
      console.error("Erro ao criar a turma: ", response.statusText);
    }
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
      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.name = alunos[aluno].RA;
      checkbox.id = alunos[aluno].RA;
      const label = document.createElement("label");
      label.textContent = alunos[aluno].nome;
      label.htmlFor = alunos[aluno].RA;
      divListarAlunos.appendChild(checkbox);
      divListarAlunos.appendChild(label);
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