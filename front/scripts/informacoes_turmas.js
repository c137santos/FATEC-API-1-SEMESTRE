async function preencher_info_turma(id) {
  const turma = await obter_turma(id);
  const PesoCiclo = await listar_ciclos_turma(id);
  const alunos = await listar_alunos_turma(id);
  const notasAlunos = await listar_notas_alunos(id);

  console.log(turma["nome"]);
  console.log(turma.professor);
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

      cicloPeso.appendChild(NomeCiclo);
      cicloPeso.appendChild(PesoNota);
    }
    exibirAlunos(alunos, notasAlunos);
  }
}

function exibirAlunos(alunos, notasAlunos, PesoCiclo) {
  const container = document.querySelector(".corpo_tabela");

  for (const chave in alunos) {
    if (alunos.hasOwnProperty(chave)) {
      const aluno = alunos[chave];
      const alunoSquare = criarComponenteAluno(aluno, notasAlunos);
      container.appendChild(alunoSquare);
      adicionarMediaAoAluno(aluno.RA, notasAlunos, PesoCiclo);
    }
  }
}

function criarComponenteAluno(aluno, notasAlunos) {
  const nomeAluno = aluno.nome;
  const alunoId = aluno.RA;

  const alunoSquare = document.createElement("div");
  alunoSquare.className = "aluno-square";
  alunoSquare.id = `${alunoId}`;

  const elementoNomeAluno = document.createElement("p");
  elementoNomeAluno.className = "aluno";
  elementoNomeAluno.textContent =
    nomeAluno.charAt(0).toUpperCase() + nomeAluno.slice(1);

  alunoSquare.appendChild(elementoNomeAluno);

  const campoNota = document.createElement("div");
  campoNota.className = "campoNota";

  for (const notaChave in notasAlunos) {
    if (notasAlunos.hasOwnProperty(notaChave)) {
      const notaAluno = notasAlunos[notaChave];
      const notaAlunoId = notaAluno.id_aluno;
      const id_ciclo = notaAluno.id_ciclo;
      const valorNota = notaAluno.valor;

      if (notaAlunoId == alunoId) {
        const InputNotas = document.createElement("input");
        InputNotas.className = "valor";
        InputNotas.type = "number";
        InputNotas.value = valorNota;
        InputNotas.id = id_ciclo;

        if (valorNota == 0) {
          InputNotas.value = "";
        }

        // Verifique se a nota já foi atribuída para torná-la somente leitura
        if (CicloAberto(id_ciclo)) {
          InputNotas.setAttribute("readonly", true);
        }

        campoNota.appendChild(InputNotas);
      }
    }
  }
  alunoSquare.appendChild(campoNota);

  return alunoSquare;
}

function adicionarMediaAoAluno(alunoId, notasAlunos, PesoCiclo) {
  const alunoSquare = document.getElementById(`${alunoId}`);
  const mediaAluno = document.createElement("div");
  mediaAluno.className = "media";
  mediaAluno.textContent = "Média";

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
