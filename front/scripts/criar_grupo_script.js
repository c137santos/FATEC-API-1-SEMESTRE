// Variáveis globais para armazenar o estado atual
let turmas = [];
let grupos = [];
let alunosNoGrupo = [];

// Função para carregar turmas e grupos do arquivo JSON (simulado)
async function carregarDados() {
    try {
        const response = await fetch("http://127.0.0.1:8080/api/v1/turmas/listar");
        const listaTurmas = await response.json();
        debugger
        turmas = listaTurmas.turmas;
        grupos = turmas.reduce((acc, turma) => acc.concat(turma.grupos), []);

        // Preencher o select com as turmas
        preencherTurmasNoSelect();
    } catch (error) {
        console.error(error);
    }
}

// Função para preencher o select com as turmas
function preencherTurmasNoSelect() {
    const selectTurma = document.getElementById('selecionar-turma');

    turmas.forEach(turma => {
        const option = document.createElement('option');
        option.value = turma.id;
        option.textContent = turma.nome;
        selectTurma.appendChild(option);
    });

    // Adicione eventos para atualizar as listas de alunos
    selectTurma.addEventListener('change', function () {
        const turmaId = selectTurma.value;
        preencherListaAlunos(turmaId); // Preencha a lista de todos os alunos
        preencherAlunosSemGrupo(turmaId); // Preencha a lista de alunos sem grupo
    });
}
// Função para preencher a lista de alunos da turma que ainda não estão em nenhum grupo

function preencherAlunosSemGrupo(turmaId) {
    const listaAlunosSemGrupo = document.getElementById('alunos-sem-grupo');
    listaAlunosSemGrupo.innerHTML = '';

    const turmaSelecionada = turmas.find(turma => turma.id === turmaId);

    if (turmaSelecionada) {
        // Filtrar os alunos que não estão em nenhum grupo
        const alunosSemGrupo = turmaSelecionada.alunos.filter(aluno => !aluno.grupo);
        debugger

        alunosSemGrupo.forEach(aluno => {
            const listItem = document.createElement('li');
            listItem.textContent = aluno.nome;
            listItem.dataset.id = aluno.id; // Para referência futura
            listItem.addEventListener('click', moverAluno);
            listaAlunosSemGrupo.appendChild(listItem);
        });
    }
}

// Função para atualizar a lista de alunos da turma selecionada
function atualizarListaAlunosDaTurma() {
    console.log('Função atualizarListaAlunosDaTurma foi chamada.');
    const listaAlunosNaTurma = document.getElementById('alunos-na-turma');
    listaAlunosNaTurma.innerHTML = '';

    // Obtém o ID da turma selecionada
    const idTurmaSelecionada = parseInt(document.getElementById('selecionar-turma').value);

    // Preencha a lista com os alunos da turma
    const turmaSelecionada = turmas.find(turma => turma.id === idTurmaSelecionada);

    turmaSelecionada.alunos.forEach(aluno => {
        const listItem = document.createElement('li');
        listItem.textContent = aluno.nome;
        listaAlunosNaTurma.appendChild(listItem);
    });
}

// Atualize a lista de alunos da turma quando uma turma for selecionada
document.getElementById('selecionar-turma').addEventListener('change', atualizarListaAlunosDaTurma);


// Função para atualizar a lista de alunos nas colunas
function atualizarListasAlunos() {
    const alunosSemGrupo = document.getElementById('alunos-sem-grupo');
    const alunosNoGrupo = document.getElementById('alunos-no-grupo'); // Corrigir essa linha

    // Limpar as listas
    alunosSemGrupo.innerHTML = '';
    alunosNoGrupo.innerHTML = '';

    // Obtém o ID da turma selecionada
    const idTurmaSelecionada = parseInt(document.getElementById('selecionar-turma').value);

    // Preenche as listas com os alunos
    const turmaSelecionada = turmas.find(turma => turma.id === idTurmaSelecionada);

    turmaSelecionada.alunos.forEach(aluno => {
        if (grupos.some(grupo => grupo.turmaId === idTurmaSelecionada && grupo.alunos.includes(aluno.id))) {
            // Aluno já está em um grupo
            const listItem = document.createElement('li');
            listItem.textContent = aluno.nome;
            alunosNoGrupo.appendChild(listItem);
        } else {
            // Aluno não está em um grupo
            const listItem = document.createElement('li');
            listItem.textContent = aluno.nome;
            alunosSemGrupo.appendChild(listItem);
        }
    });
}

// Evento de carregamento da página
document.addEventListener('DOMContentLoaded', async function () {
    await carregarDados();
    atualizarListaAlunosDaTurma();
});

// Evento de clique no botão "Salvar Grupo"
document.getElementById('salvar-grupo').addEventListener('click', function () {
    // Captura o nome do grupo e o ID da turma selecionada
    const nomeGrupo = document.getElementById('nome-grupo').value;
    const idTurma = parseInt(document.getElementById('selecionar-turma').value);

    // Obtém a lista de alunos no grupo
    const listaAlunosNoGrupo = Array.from(alunosNoGrupo.getElementsByTagName('li'));
    const alunosNoGrupoNomes = listaAlunosNoGrupo.map(item => item.textContent);

    // Crie a pop-up de confirmação
    const confirmacao = confirm(
        `Nome do Grupo: ${nomeGrupo}\nTurma Selecionada: Turma ${idTurma}\nAlunos no Grupo: ${alunosNoGrupoNomes.join(', ')}\n\nDeseja confirmar a criação do grupo?`
    );

    if (confirmacao) {
        // Lógica para salvar o grupo
        // Você pode implementar a lógica de salvar o grupo aqui
        // Por enquanto, apenas exibiremos uma mensagem de confirmação
        alert('Grupo criado com sucesso!');
    }
});

// Evento de clique no botão "Editar Grupo"
document.getElementById('editar-grupo').addEventListener('click', function () {
    // Implementar a lógica para editar um grupo existente @Ruth
});

// Evento de busca de alunos
document.getElementById('buscar-aluno').addEventListener('input', function () {
    // Captura o termo de busca
    const termoBusca = document.getElementById('buscar-aluno').value.toLowerCase();

    // Obtém todas as listas de alunos
    const listaAlunosSemGrupo = Array.from(document.getElementById('alunos-sem-grupo').getElementsByTagName('li'));
    const listaAlunosNoGrupo = Array.from(document.getElementById('alunos-no-grupo').getElementsByTagName('li'));

    // Filtra e exibe/oculta os alunos com base no termo de busca
    listaAlunosSemGrupo.forEach(item => {
        const texto = item.textContent.toLowerCase();
        // Se o nome do aluno contiver o termo de busca, exiba-o; caso contrário, oculte-o
        item.style.display = texto.includes(termoBusca) ? 'block' : 'none';
    });

    listaAlunosNoGrupo.forEach(item => {
        const texto = item.textContent.toLowerCase();
        // Se o nome do aluno contiver o termo de busca, exiba-o; caso contrário, oculte-o
        item.style.display = texto.includes(termoBusca) ? 'block' : 'none';
    });
});