async function preencher_info_turma(id) {
  const turma = await obter_turma(id);
  const PesoCiclo = await listar_ciclos_turma(id);
  const alunos = await listar_alunos_turma(id);
  const notasAlunos = await listar_notas_alunos(id);

  if (turma) {
    const nomeTurmaElement = document.querySelector(".fnomeTurma");
    const nomeProfessorElement = document.querySelector(".fnomeProfessor");
    const cicloPeso = document.querySelector(".ciclo-peso");
    nomeTurmaElement.textContent = "Nome turma: " + turma["nome"];
    nomeProfessorElement.textContent = "Nome professor: " + turma["professor"];
    for (let chave in PesoCiclo) {
      const pesoData = PesoCiclo[chave];

      const NomeCiclo = document.createElement("span");
      NomeCiclo.className = "ciclo";
      NomeCiclo.innerHTML = `C${pesoData.numero_ciclo}:`;

      const PesoNota = document.createElement("span");
      PesoNota.className = "peso";
      PesoNota.textContent = pesoData.peso_nota;
      PesoNota.id = `pesoCiclo=${pesoData.numero_ciclo}`;
      cicloPeso.appendChild(NomeCiclo);
      cicloPeso.appendChild(PesoNota);
    }
    // Chama a função para iniciar a criação do componentes dos alunos
    exibirAlunos(alunos, notasAlunos, cicloPeso);
  }
}

function exibirAlunos(alunos, notasAlunos, cicloPeso) {
  const container = document.querySelector(".corpo_tabela");

  for (const chave in alunos) {
    if (alunos.hasOwnProperty(chave)) {
      const aluno = alunos[chave];
      const nomeAluno = aluno.nome; // Pega o nome do aluno
      const alunoId = chave; // A chave do objeto aluno é o seu ID
      console.log(`id do aluno: ${alunoId}`);
      //Chama a função para criar o alunoSquare de cada aluno
      const alunoSquare = criarComponenteAluno(alunoId, nomeAluno, notasAlunos);
      container.appendChild(alunoSquare);
      //Chama a função para criar o campo de media de cada aluno
      adicionarMediaAoAluno(alunoId, notasAlunos, cicloPeso);
    }
  }
}

function criarComponenteAluno(alunoId, nomeAluno, notasAlunos) {
  const alunoSquare = document.createElement("div");
  alunoSquare.className = "aluno-square";
  alunoSquare.id = `alunoId=${alunoId}`;

  const elementoNomeAluno = document.createElement("p");
  elementoNomeAluno.className = "aluno";
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
      const id_turma = notaAluno.id_turma;
      const id_aluno = notaAluno.id_aluno;
      const id_ciclo = notaAluno.id_ciclo;
      const valorNota = notaAluno.valor;

      if (id_aluno == alunoId) {
        const InputNotas = document.createElement("input");
        InputNotas.className = "valor";
        InputNotas.type = "number";
        InputNotas.value = valorNota;
        InputNotas.id = `id_turma=${id_turma},id_aluno=${id_aluno},id_ciclo=${id_ciclo}`;

        if (valorNota == 0) {
          InputNotas.value = "";
        }

        //Verifica se a nota esta aberta para edição
        if (CicloAberto(id_ciclo)) {
          InputNotas.setAttribute("readonly", true);
        }

        campoNota.appendChild(InputNotas);
      }
    }
  }

  return campoNota;
}

function adicionarMediaAoAluno(alunoId, notasAlunos, PesoCiclo) {
  const alunoSquare = document.getElementById(`alunoId=${alunoId}`);
  const mediaAluno = document.createElement("div");
  mediaAluno.className = "media";
  mediaAluno.textContent = "media";
  mediaAluno.id = `mediaAlunoId=${alunoId}`;

  alunoSquare.appendChild(mediaAluno);
}

// Função que verifica se o ciclo está aberto
function CicloAberto(id_ciclo) {
  return true;
}

async function listar_ciclos_turma(id) {
  const response = await fetch(
    `http://localhost:8080/api/v1/ciclos/listar/${id}`,
    { method: "GET" }
  );
  const PesoCiclo = await response.json();
  console.log(PesoCiclo);
  return PesoCiclo;
}

async function listar_alunos_turma(id) {
  const response = await fetch(
    `http://localhost:8080/api/v1/turmas_alunos/listar_alunos_da_turma/${id}`,
    { method: "GET" }
  );
  const alunos = await response.json();
  console.log(alunos);
  return alunos;
}

async function listar_notas_alunos(id) {
  const response = await fetch(
    `http://localhost:8080/api/v1/notas/turma/listar/${id}`,
    { method: "GET" }
  );
  const notasAlunos = await response.json();
  console.log(notasAlunos);
  return notasAlunos;
}

async function obter_turma(id) {
  const resposta = await fetch(
    `http://localhost:8080/api/v1/turmas/listar/${id}`,
    { method: "GET" }
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
