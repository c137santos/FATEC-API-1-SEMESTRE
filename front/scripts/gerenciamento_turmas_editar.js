async function preencher_campos_formulario(id){
    const turma = await obter_turma(id)
    if(turma){
        const dataFormatada = turma["data_de_inicio"].split('/').reverse().join('-');
        document.getElementById('fnome')['value'] = turma["nome"]
        document.getElementById('fprofessor')['value'] = turma["professor"]
        document.getElementById('fdata')['value'] = dataFormatada
        document.getElementById('fduracaosCiclo')['value'] = parseInt(turma["duracao_ciclo"])
        document.getElementById('fquantidadeCiclo').style.backgroundColor = "white";
        document.getElementById('fquantidadeCiclo').innerText = turma["quantidade_ciclos"];
        // TODO, melhorar o fquantidadeciclo do CSS disso aqui
    } else {
        alert("Falha ao preencher os campos do formulário!\nA turma não foi encontrada.")
    }
}
async function requisitar_editar_turma(id){
    const alunos_adicionados = pegarAlunosSelecionados(alunos_todos)
    const decisao_usuario = criar_modal_confirmar_edicao();
    if(decisao_usuario){
        const dataPreenchida = document.getElementById('fdata')['value']
        const dataPreenchidaForm = moment(dataPreenchida).format("DD/MM/YYYY"); 
        const turma = {
            "nome" : document.getElementById('fnome')['value'],
            "professor" : document.getElementById('fprofessor')['value'],
            "data_de_inicio" : dataPreenchidaForm,
            "duracao_ciclo": document.getElementById('fduracaosCiclo')['value'],
            "alunos_adicionados": alunos_adicionados
        }
        fetch (`http://localhost:8080/api/v1/turmas/editar/${id}`,{method: "POST", body:JSON.stringify(turma)})
            .then(() => window.location.href = 'editar_turma.html?id=' + id)
    }
}
/** Obtém uma turma pelo id
 * @param {string} id - o identificador único da turma.
 * @returns {object} retornará undefined ou um objeto contendo os atributos nome, professor e data_de_inicio.
*/
async function obter_turma(id) {
    const resposta = await fetch (`http://localhost:8080/api/v1/turmas/listar/${id}`, {method: "POST"})
    const turma = await resposta.json()
    console.log(turma)
    return turma
}
/** Recupera o id da turma presente como consulta na URL
 * @returns {string} id - o identificador único
*/
function obter_id(){ return new URLSearchParams(window.location.search).get('id') }
/** Cria um modal para a confirmação do usuário
 * @return {boolean} resposta - decisão do usuário
*/
function criar_modal_confirmar_edicao(){
    const mensagem = "Atenção! Os dados da turma serão modificados.\nDeseja prosseguir com a edição?"
    return window.confirm(mensagem);
}

let alunos_todos = listarAlunos()

async function listarAlunos(){
    try {
        const response = await fetch(
        "http://127.0.0.1:8080/api/v1/alunos/listar"
        );
        alunos_todos = await response.json();
    } catch (error) {
        console.error("Erro ao buscar dados da API -> ", error);
        return null;
    }finally{
        console.log(alunos_todos)
        addAlunos(alunos_todos)
        return alunos_todos

    }
}

function addAlunos(alunos) {
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

