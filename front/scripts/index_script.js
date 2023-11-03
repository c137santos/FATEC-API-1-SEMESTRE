function redirecionarParaPagina(id) {
    if (id === 'turma') {
        window.location.href = 'gerenciamento_turmas.html';
    } else if (id === 'aluno') {
        window.location.href = 'gerenciamento_aluno.html';
    } else if (id === 'grupos') {
        window.location.href = 'listar_grupo.html';
    } else if (id === 'global-settings') {
        window.location.href = 'global_settings.html';
    } else {
        window.location.href = 'pagina-padrao.html';
    }
}

document.getElementById('turma').addEventListener('click', function() {
    redirecionarParaPagina('turma');
});

document.getElementById('aluno').addEventListener('click', function() {
    redirecionarParaPagina('aluno');
});

