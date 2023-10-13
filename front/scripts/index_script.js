function redirecionarParaPagina(id) {
    if (id === 'turma') {
        window.location.href = 'gerenciamento_turmas.html';
    } else if (id === 'aluno') {
        window.location.href = 'pagina-aluno.html';
    } else if (id === 'grupos') {
        window.location.href = 'pagina-grupos.html';
    } else if (id === 'global-settings') {
        window.location.href = 'pagina-global-settings.html';
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

document.getElementById('grupos').addEventListener('click', function() {
    redirecionarParaPagina('grupos');
});

document.getElementById('global-settings').addEventListener('click', function() {
    redirecionarParaPagina('global-settings');
});