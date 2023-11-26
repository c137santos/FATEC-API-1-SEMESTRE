function redirecionarParaPagina(id) {
    if (id === 'turma') {
        window.location.href = 'gerenciamento_turmas.html';
    } else if (id === 'aluno') {
        window.location.href = 'gerenciamento_aluno.html';
    } else if (id === 'global_settings') {
        window.location.href = 'global_settings.html';
    } else if (id == 'relatorio'){
        window.location.href = 'relatorio.html';
    } else if (id == 'importar-aluno'){
        window.location.href = 'importacao_alunos.html';
    }else if (id == 'exportar'){
        window.location.href = 'exportacao_relatorio.html';
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

document.getElementById('global_settings').addEventListener('click', function() {
    redirecionarParaPagina('global_settings');
});

document.getElementById('relatorio').addEventListener('click', function() {
    redirecionarParaPagina('relatorio');
});

document.getElementById('importar-aluno').addEventListener('click', function() {
    redirecionarParaPagina('importar-aluno');
});

document.getElementById('exportar').addEventListener('click', function() {
    redirecionarParaPagina('exportar');
});