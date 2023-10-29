// Função para buscar turmas no servidor
let turmaData;
async function GetTurmas() {
  try {
    const response = await fetch("http://127.0.0.1:8080/api/v1/turmas/listar");
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
      imagemIcon.addEventListener("click",() => requisitar_excluir_turma(`${turmaId}`))

      const imagemIconEdit = document.createElement("img")
      imagemIconEdit.src = "../front/icon/edit-icon.svg"
      imagemIconEdit.alt ="Icone"
      imagemIconEdit.className = "edit-icon"
      imagemIconEdit.id = `${turmaId}`;
      imagemIconEdit.addEventListener("click",() => requisitar_editar_turma(`${turmaId}`))

      // Adiciona o ícone ao turmaSquare
      turmaSquare.appendChild(imagemIcon);
      turmaSquare.appendChild(imagemIconEdit);

      // Adiciona o turmaSquare ao container
      container.appendChild(turmaSquare);
    }
  }
}

const addTurmaButton = document.querySelector(".add-turma-button");
addTurmaButton.addEventListener("click", showModal);

// Função para mostrar o modal
async function showModal() {
  const modal = document.getElementById("myModal");
  modal.style.display = "block";
}

// Função para fechar o modal
function closeModal() {
  const modal = document.getElementById("myModal");
  modal.style.display = "none";
}

//aciona evento para abrir a tela de confirmacao e editar a criacao de turma
const criarTurmaButton = document.querySelector(".submit-turma");
criarTurmaButton.addEventListener("click", coletaDadosNovaTurma);

//aciona evento para fechar a tela de confirmacao e editar a criacao de turma
const cancelarButton = document.getElementById("cancelarButton");
cancelarButton.addEventListener("click", closeConfirmacao);

// Função para abrir tela e coletar os dados da nova turma
async function coletaDadosNovaTurma() {
  const turmaNome = document.getElementById("turmaNome").value;
  const professor = document.getElementById("professor").value;
  const dataInicio = document.getElementById("dataInicio").value;
  const duracaoCiclo = document.getElementById("duracaoCiclo").value;
  console.log(dataInicio);

  const regex = /^[a-zA-Z \s]*$/;
  for (let id in turmaData) {
    if (turmaData[id].nome == turmaNome) {
      alert("O Nome da Turma já existe.");
      return;
    }
  }
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
  const dia = String(data.getDate()).padStart(2, '0'); // Garante que o dia tenha sempre 2 dígitos
  const mes = String(data.getMonth() + 1).padStart(2, '0'); // Garante que o mês tenha sempre 2 dígitos
  const ano = data.getFullYear();
  // const dataFormatada = `${dia}/${mes}/${ano}`;

  if (ano < 1000 || ano > 9999) {
    alert("O ano deve ter exatamente 4 dígitos.");
    return;
  }
  
  const dataFormatada = dataInicio.split('-').reverse().join('/');

  // Construir o objeto de turma
  const novaTurmaData = {
    nome: turmaNome,
    professor: professor,
    data_de_inicio: dataFormatada,
    duracao_ciclo: duracaoCiclo,
    quantidade_ciclos: 4
  };

  console.log(novaTurmaData)

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
    const response = await fetch(
      `http://127.0.0.1:8080/api/v1/turmas/criar`,
      {
        method: "POST",
        body: JSON.stringify(novaTurmaData),
      }
    );

    // Verifica se a resposta da solicitação está OK (status 200)
    if (response.ok) {
      const resposta = await response.json();
      const mensagem = resposta.mensagem;
      const detalhes = resposta.detalhes;
      alert("Resposta do servidor:\n" + mensagem + "\n" + detalhes.join("\n"));
      window.location.href = 'gerenciamento_turmas.html'
    } else {
      // Lida com erros de resposta, se houver
      console.error("Erro ao criar a turma: ", response.statusText);
    }
  } catch (error) {
    console.error("Erro ao enviar os dados para o servidor: " + error);
  }
}

function requisitar_excluir_turma(id){
  if(window.confirm("Atenção! A turma será excluída.\nDeseja prosseguir?")){
    fetch(`http://localhost:8080/api/v1/turmas/excluir/${id}`,{method:'POST'}).then(document.getElementById(id).remove())
  }  
}


function requisitar_editar_turma(id) {
  window.location.href = 'editar_turma.html?id=' + id;
}


GetTurmas();
