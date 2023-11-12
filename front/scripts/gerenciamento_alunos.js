let idAluno = "";
let editar_aluno = false;
getInfoAlunos();
let alunos_todos = {};
async function getInfoAlunos() {
  try {
    const response = await fetch("http://127.0.0.1:8080/api/v1/alunos/listar");
    alunos_todos = await response.json();
    mostraAlunos(alunos_todos);
  } catch (error) {
    console.error("Erro ao buscar dados da API -> ", error);
    return null;
  }
}

const renderizarAluno = (aluno) => {
  const quadrado = document.createElement("div");
  quadrado.className = "quadrado";

  const labelRa = document.createElement("p");
  labelRa.textContent = `RA: ${aluno.RA}`;

  quadrado.appendChild(labelRa);

  const labelNome = document.createElement("p");
  labelNome.textContent = aluno.nome;
  quadrado.appendChild(labelNome);

  const labelGenero = document.createElement("p");
  labelGenero.textContent = aluno.genero;
  quadrado.appendChild(labelGenero);

  const labelIdade = document.createElement("p");
  labelIdade.textContent = aluno.data_nascimento;
  quadrado.appendChild(labelIdade);

  alunos = document.getElementById("aluno-container");
  const imagemIconEdit = document.createElement("img");
  imagemIconEdit.src = "../front/icon/edit-icon.svg";
  imagemIconEdit.alt = "Icone";
  imagemIconEdit.className = "edit-icon";
  imagemIconEdit.id = `${aluno.RA}`;
  imagemIconEdit.addEventListener("click", () => editarAluno(`${aluno.RA}`));
  quadrado.appendChild(imagemIconEdit);

  const imagemIconDelete = document.createElement("img");
  imagemIconDelete.src = "../front/icon/trash-icon.svg";
  imagemIconDelete.alt = "Icone";
  imagemIconDelete.className = "trash-icon";
  imagemIconDelete.id = `delete${aluno.RA}`;
  imagemIconDelete.addEventListener("click", () => deleteAluno(`${aluno.RA}`));
  quadrado.appendChild(imagemIconDelete);
  alunos.appendChild(quadrado);

  quadrado.addEventListener("click", async (e) => {
    if (editar_aluno == false) {
      let turmasALuno = await getTurmasAluno(aluno.RA);
      idAluno = aluno.RA;
      const id = e.target.id;
      const info = document.createElement("dialog");
      info.id = "detalhes-aluno";
      info.className = "dialog";
      info.innerHTML = `
    <div class="dialog-header">
        <h2 class="dialog-title">Detalhes do aluno ${id}</h2>
        </div>
        <div class="dialog-body">
        <p>RA: ${aluno.RA}</p>
        <p>Nome: ${aluno.nome}</p>
        <p>Gênero: ${aluno.genero}</p>
        <p>Data de nascimento: ${aluno.data_nascimento}</p>
        </div>
        <div>
        <p> Escolha a turma:</p>
        <select id="select-turmas">
          <option value="" selected></option>
        </select>
        <div id="mostraNotas"> 
           <p> Notas da turma:</p>
        </div>
        </div>
        <button onclick="fechaDialogo()">Fechar</button>
        `;
      document.body.appendChild(info);
      info.showModal();
      selectTurmas(turmasALuno);
    }
  });
};

function fechaDialogo() {
  dialogo = document.getElementById("detalhes-aluno");
  dialogo.close();
  window.location.reload(false);
}

const mostraAlunos = (alunos) => {
  for (const id in alunos) {
    renderizarAluno(alunos[id]);
  }
};

async function editarAluno(RA) {
  editar_aluno = true;
  let aluno = alunos_todos[RA];
  const modal = document.createElement("dialog");

  const titulo = document.createElement("h1");
  titulo.textContent = "Editar aluno";
  modal.appendChild(titulo);

  const formulario = document.createElement("form");
  modal.appendChild(formulario);

  const aluno_label = document.createElement("p");
  aluno_label.textContent = "Nome";
  const inputNome = document.createElement("input");
  inputNome.type = "text";
  inputNome.value = aluno.nome;
  formulario.appendChild(aluno_label);
  formulario.appendChild(inputNome);

  const aluno_genero = document.createElement("p");
  aluno_genero.textContent = "Genero";
  const selecionarGenero = document.createElement("select");
  selecionarGenero.id = "generoNovoAluno";
  const opcoesGenero = [
    "Homem cis",
    "Mulher cis",
    "Homem trans",
    "Mulher trans",
    "Gênero neutro",
    "Não-binário",
  ];
  opcoesGenero.forEach(function (opcao) {
    const option = document.createElement("option");
    option.text = opcao;
    option.value = opcao;
    selecionarGenero.appendChild(option);
  });

  const generoAtual = opcoesGenero.find(
    (opcao) => opcao === aluno.genero
  );
  if (generoAtual) {
    selecionarGenero.value = generoAtual;
  }
  formulario.appendChild(aluno_genero);
  formulario.appendChild(selecionarGenero);

  const aluno_nasc = document.createElement("p");
  aluno_nasc.textContent = "data de nascimento:";
  const inputDataNascimento = document.createElement("input");
  inputDataNascimento.type = "date";
  inputDataNascimento.value = aluno.data_nascimento;
  formulario.appendChild(aluno_nasc);
  formulario.appendChild(inputDataNascimento);

  // Adicione um botão de salvar ao formulário
  const buttonSalvar = document.createElement("button");
  buttonSalvar.textContent = "Salvar";
  formulario.appendChild(buttonSalvar);

  // Adicione o modal à página
  document.body.appendChild(modal);

  modal.showModal();

  buttonSalvar.addEventListener("click", async () => {
    // Obter os valores do formulário
    const nome = inputNome.value;
    if (nome === "") {
      alert("O Nome do aluno é obrigatório.");
      return;
    }
    const genero = inputGenero.value;
    if (genero === "") {
      alert("O gênero do aluno é obrigatório.");
      return;
    }
    const dataNascimento = inputDataNascimento.value;
    if (dataNascimento === "") {
      alert("A data de nascimento do aluno é obrigatório.");
      return;
    }

    let dataNascimentoForm = moment(dataNascimento).format("DD/MM/YYYY");

    const aluno_editado = {
      RA: RA,
      nome: nome,
      genero: genero,
      data_nascimento: dataNascimentoForm,
    };

    const response = await backEditarAluno(aluno_editado);
    modal.close();
    editar_aluno = false;
    event.preventDefault();
  });
}

async function backEditarAluno(aluno_editado) {
  try {
    const response = await fetch(
      `http://127.0.0.1:8080/api/v1/alunos/editar/${aluno_editado.RA}`,
      { method: "POST", body: JSON.stringify(aluno_editado) }
    );
    return response.status === 200;
  } catch (error) {
    console.error("Erro ao buscar dados da API -> ", error);
    return false;
  }
}

const deleteAluno = (RA) => {
  try {
    fetch(`http://127.0.0.1:8080/api/v1/alunos/deletar/${RA}`, {
      method: "POST",
    });
    console.log("chamou o deletar");
  } catch (error) {
    console.error("Erro ao buscar dados da API -> ", error);
  }
};
var favDialog = document.getElementById("favDialog");
var botaoNovoAluno = document.getElementById("buttonNovoAluno");
var submitButton = document.getElementById("submit");

botaoNovoAluno.addEventListener("click", function () {
  favDialog.showModal();
});

submitButton.addEventListener("click", function () {
  criarNovoAluno();
  favDialog.close();
});

const criarNovoAluno = () => {
  nomeNovo = document.getElementById("nomeNovoALuno").value;
  if (nomeNovo === "") {
    alert("o nome do aluno é obrigatório");
    return;
  }
  generoNovo = document.getElementById("generoNovoAluno").value;
  if (generoNovo === "") {
    alert("o gênero do aluno é obrigatório");
    return;
  }
  dataNascNova = document.getElementById("dataNascNovoAluno").value;
  if (dataNascNova === "") {
    alert("a data de nascimento do aluno é obrigatório");
    return;
  }

  const dataNascNovaForm = moment(dataNascNova).format("DD/MM/YYYY");

  const alunoNovo = {
    nome: nomeNovo,
    genero: generoNovo,
    data_nascimento: dataNascNovaForm,
  };
  try {
    fetch("http://127.0.0.1:8080/api/v1/alunos/criar", {
      method: "POST",
      body: JSON.stringify(alunoNovo),
    });
    console.log("chamou o back");
  } catch (error) {
    console.error("Erro ao buscar dados da API -> ", error);
  }
};

async function getTurmasAluno(RA) {
  try {
    const response = await fetch(
      `http://127.0.0.1:8080/api/v1/turmas_alunos/listar_turmas_do_aluno/${RA}`
    );
    turmasAluno = await response.json();
  } catch (error) {
    console.error("Erro ao buscar dados da API -> ", error);
  } finally {
    return turmasAluno;
  }
}

function selectTurmas(turmaAluno) {
  const select = document.getElementById("select-turmas");
  for (let turma in turmaAluno) {
    let option = document.createElement("option");
    option.id = turma;
    option.value = turma;
    option.textContent = turmaAluno[turma].nome;
    select.appendChild(option);
  }
  select.onchange = (event) => {
    var turmaId = event.target.value;
    getNotasALunoTurma(turmaId);
  };
}

async function getNotasALunoTurma(turmaId) {
  try {
    const response = await fetch(
      `http://127.0.0.1:8080/api/v1/notas/aluno/listar/${idAluno}`
    );
    notasAluno = await response.json();
  } catch (error) {
    console.error("Erro ao buscar dados da API -> ", error);
  } finally {
    for (let nota in notasAluno) {
      if (notasAluno[nota].id_turma == turmaId) {
        MostraNotas(notasAluno[nota].id_ciclo, notasAluno[nota].valor);
      }
    }
  }
}

function MostraNotas(ciclo, valor) {
  dialogALuno = document.getElementById("mostraNotas");
  valorNota = document.createElement("p");
  valorNota.textContent = `Ciclo: ${ciclo} | Valor: ${valor}`;
  dialogALuno.appendChild(valorNota);
}
