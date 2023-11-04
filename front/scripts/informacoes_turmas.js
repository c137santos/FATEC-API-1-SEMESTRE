async function preencher_info_turma(id) {
  const turma = await obter_turma(id);
  const PesoCiclo = await listar_ciclos_turma(id);
  const alunos = await listar_alunos_turma(id);
  const notasAlunos = await listar_notas_alunos(id);

  if (turma) {
    const nomeTurmaElement = document.querySelector(".fnomeTurma");
    const nomeProfessorElement = document.querySelector(".fnomeProfessor");
    const cicloPeso = document.querySelector(".ciclo-peso");
    const quantidadeAlunosElement = document.getElementById('fquantidadeAlunos');
    const dataInicioElement = document.getElementById('fdataInicio');
    nomeTurmaElement.textContent = turma["nome"];
    nomeProfessorElement.textContent = turma["professor"];
    quantidadeAlunosElement.innerText = alunos ? Object.keys(alunos).length : 0;
    dataInicioElement.innerText = turma["data_de_inicio"];
    for (let chave in PesoCiclo) {
      const pesoData = PesoCiclo[chave];
      const NomeCiclo = document.createElement("label");
      NomeCiclo.className = "ciclo";
      NomeCiclo.htmlFor = `pesoCiclo=${chave}`
      NomeCiclo.innerHTML = `C${pesoData.numero_ciclo}:`;

      const PesoNota = document.createElement("input");
      PesoNota.className = "peso";
      PesoNota.id = `pesoCiclo=${chave}`
      PesoNota.value = pesoData.peso_nota;

      PesoNota.addEventListener("keypress", (e) => { 
        if(e.key === 'Enter'){
          requisitar_salvar_ciclo_peso() 
        }
      });

      cicloPeso.appendChild(NomeCiclo);
      cicloPeso.appendChild(PesoNota);
    }

    // Chama a função para iniciar a criação do componentes dos alunos
    exibirAlunos(alunos, notasAlunos, cicloPeso, id);
  }
}

function exibirAlunos(alunos, notasAlunos, cicloPeso, id_turma) {
  const container = document.querySelector(".corpo_tabela");

  for (const chave in alunos) {
    if (alunos.hasOwnProperty(chave)) {
      const aluno = alunos[chave];
      const nomeAluno = aluno.nome; // Pega o nome do aluno
      const alunoId = chave; // A chave do objeto aluno é o seu ID
      //Chama a função para criar o alunoSquare de cada aluno
      const alunoSquare = criarComponenteAluno(alunoId, nomeAluno, notasAlunos);
      container.appendChild(alunoSquare);
      //Chama a função para criar o campo de media de cada aluno
      adicionarMediaAoAluno(alunoId, notasAlunos, cicloPeso, id_turma);
    }
  }
}

function criarComponenteAluno(alunoId, nomeAluno, notasAlunos) {
  const alunoSquare = document.createElement("div");
  alunoSquare.className = "aluno-square";
  alunoSquare.id = `alunoId=${alunoId}`;

  const elementoNomeAluno = document.createElement("p");
  elementoNomeAluno.className = "aluno";
  elementoNomeAluno.id = `${alunoId}`;
  elementoNomeAluno.textContent =
    nomeAluno.charAt(0).toUpperCase() + nomeAluno.slice(1);

  alunoSquare.appendChild(elementoNomeAluno);

  // Chama a função para criar campo de notas para cada aluno
  const campoNota = criarCampoNota(alunoId, notasAlunos);
  alunoSquare.appendChild(campoNota);

  return alunoSquare;
}

function criarCampoNota(alunoId, notasAlunos) {
  const campoNota = document.createElement("div");
  campoNota.className = "campoNota";

  for (const notaChave in notasAlunos) {
    if (notasAlunos.hasOwnProperty(notaChave)) {
      const notaAluno = notasAlunos[notaChave];
      const id_nota = notaChave;
      const id_turma = notaAluno.id_turma;
      const id_aluno = notaAluno.id_aluno;
      const id_ciclo = notaAluno.id_ciclo;
      const cicloAberto = notaAluno.edicao_habilitada;
      const valorNota = notaAluno.valor;
      

      if (id_aluno == alunoId) {
        const InputNotas = document.createElement("input");
        InputNotas.className = "valor";
        InputNotas.type = "number";
        InputNotas.step = "0.5";
        InputNotas.min = "1";
        InputNotas.max = "10";
        InputNotas.value = valorNota;
        InputNotas.id = `id_nota=${id_nota},id_turma=${id_turma},id_aluno=${id_aluno},id_ciclo=${id_ciclo}`;

        if (cicloAberto === true) {
          const aviso_ciclo_aberto =
            document.getElementById("aviso_ciclo_aberto");
          aviso_ciclo_aberto.textContent = `Ciclo aberto para nota: ${id_ciclo}`;
          InputNotas.dataset.ValorOriginal = valorNota;
          InputNotas.removeAttribute("readonly");
        } else {
          InputNotas.setAttribute("readonly", true);
        }

        campoNota.appendChild(InputNotas);
      }
    }
  }
  return campoNota;
}

function adicionarMediaAoAluno(alunoId, notasAlunos, PesoCiclo, id_turma) {
  const alunoSquare = document.getElementById(`alunoId=${alunoId}`);
  const mediaAluno = document.createElement("div");
  mediaAluno.className = "media";
  mediaAluno.id = `mediaAlunoId=${alunoId}`;
  Promise
    .resolve(obter_fee_turma_aluno(id_turma, alunoId))
    .then((fee) => mediaAluno.textContent = fee)
  alunoSquare.appendChild(mediaAluno);
}

async function editarNota() {
  const alunos = await listar_alunos_turma(obter_id());
  requisitar_editar_nota(alunos);
}

function requisitar_editar_nota(alunos) {
  const notasEditaveis = document.querySelectorAll(".valor:not([readonly])");
  const requestBody = {};

  let notasInvalidas = false; // Variável para verificar se há notas inválidas

  notasEditaveis.forEach((nota) => {
    const id_nota = nota.id.split("id_nota=")[1].split(",")[0];
    const id_turma = nota.id.split("id_turma=")[1].split(",")[0];
    const id_aluno = nota.id.split("id_aluno=")[1].split(",")[0];
    const id_ciclo = nota.id.split("id_ciclo=")[1];
    const valor = parseFloat(nota.value); // Converter o valor para número

    if (isNaN(valor) || valor < 0 || valor > 10) {
      // Se a nota não for um número ou estiver fora do intervalo, marca como inválida
      notasInvalidas = true;
      nota.classList.add("nota-invalida"); // Adiciona uma classe para destacar a nota inválida visualmente
    } else {
      // Se a nota for válida, adiciona ao requestBody
      requestBody[id_nota] = {
        id_turma: id_turma,
        id_aluno: id_aluno,
        id_ciclo: id_ciclo,
        valor: valor,
      };
    }
  });

  if (notasInvalidas) {
    // Exibe uma mensagem de erro ao usuário
    alert("Todas as notas devem estar entre 0 e 10.");
    return;
  }

  const decisao_usuario = criar_modal_confirmar_edicao(requestBody, alunos);
  if (decisao_usuario) {
    fetch(`http://localhost:8080/api/v1/notas/editar`, {
      method: "POST",
      body: JSON.stringify(requestBody),
    });
  } else {
    // O usuário optou por não prosseguir, você pode adicionar alguma lógica aqui se necessário
  }
}

function criar_modal_confirmar_edicao(requestBody, alunos) {
  let mensagem =
    "Atenção! Os seguintes detalhes das notas serão modificados:\n\n";

  for (const idNota in requestBody) {
    if (requestBody.hasOwnProperty(idNota)) {
      const nota = requestBody[idNota];
      const id_aluno = requestBody[idNota].id_aluno;
      if (id_aluno in alunos) {
        const aluno = alunos[id_aluno];
        mensagem += `Aluno: ${aluno.nome},`;
      }
      mensagem += ` Ciclo: ${nota.id_ciclo},`;
      mensagem += ` Valor: ${nota.valor}\n\n`;
    }
  }

  mensagem += "Deseja prosseguir com a edição?";

  return window.confirm(mensagem);
}

async function listar_ciclos_turma(id) {
  const response = await fetch(
    `http://localhost:8080/api/v1/ciclos/listar/${id}`
  );
  const PesoCiclo = await response.json();
  console.log(PesoCiclo);
  return PesoCiclo;
}

async function listar_alunos_turma(id) {
  const response = await fetch(
    `http://localhost:8080/api/v1/turmas_alunos/listar_alunos_da_turma/${id}`
  );
  const alunos = await response.json();
  console.log(alunos);
  return alunos;
}

async function listar_notas_alunos(id) {
  const response = await fetch(
    `http://localhost:8080/api/v1/notas/turma/listar/${id}`
  );
  const notasAlunos = await response.json();
  console.log(notasAlunos);
  return notasAlunos;
}

async function obter_turma(id) {
  const resposta = await fetch(
    `http://localhost:8080/api/v1/turmas/listar/${id}`
  );
  const turma = await resposta.json();
  console.log(turma);
  return turma;
}
function obter_id() {
  return new URLSearchParams(window.location.search).get("id");
  //        /** Recupera o id da turma presente como consulta na URL
  //  * @returns {string} id - o identificador único
}

async function requisitar_salvar_ciclo_peso(){
  if(!confirm("Essa operação afetará o FEE dos alunos.\nDeseja prosseguir mesmo assim?")){
    return
  }
  console.log("Editando os ciclos...")
  const turma_id = obter_id()
  const ciclos = await listar_ciclos_turma(turma_id)
  for(var id_ciclo in ciclos){
    console.log(`Salvando o ciclo ${id_ciclo}`)
    elementoCiclo = document.getElementById(`pesoCiclo=${id_ciclo}`)
    ciclo = ciclos[id_ciclo]
    ciclo["peso_nota"] = elementoCiclo.value
    console.log(ciclo)
    res = await fetch(`http://localhost:8080/api/v1/ciclos/editar/${id_ciclo}`,{method:"POST", body:JSON.stringify(ciclo)})
    console.log(res)
  }
  location.reload()
}

async function obter_fee_turma_aluno(id_turma, id_aluno){
  const response = await fetch (`http://localhost:8080/api/v1/notas/fee/obter/${id_turma}/${id_aluno}`, {method: "GET"})
  const fee = await response.json()
  return fee ? fee.valor : 0.0
}
