function inicializaPaginaExportacaoRelatorio() {
    listarTurmas()
}

async function listarTurmas() {
    try {
        const response = await fetch("http://127.0.0.1:8080/api/v1/turmas/listar");
        const turmaData = await response.json()

        const opcoesTurma = document.getElementById("selecionaTurma")

        for (const turmaId in turmaData) {
            if (turmaData.hasOwnProperty(turmaId)) {
                const turma = turmaData[turmaId];
                const option = document.createElement("option");
                option.value = turmaId;
                option.dataset.nome = turma.nome;
                option.textContent = turma.nome;
                opcoesTurma.appendChild(option);
            }
        }
    } catch (error) {
        console.error("Erro ao buscar dados da API -> ", error)
    }
}

async function exportacaoRelatorio(event) {
    event.preventDefault()
    const turmaSelecionada = document.getElementById("selecionaTurma")
    const idTurma = turmaSelecionada.value
    const nomeTurma = (turmaSelecionada.options[turmaSelecionada.selectedIndex].dataset.nome).replace(/[^a-zA-Z0-9]/g, '').toLowerCase()
    try {
        const dados = await solicitaRelatorio(idTurma)
        iniciarDownload(dados, nomeTurma)
    } catch (error) {
        console.error('Erro ao exportar relatório:', error)
    }
}

async function solicitaRelatorio(idTurma) {
    try {
        const response = await fetch(`http://127.0.0.1:8080/api/v1/relatorios/${idTurma}`)
        const relatorioData = await response.json()
        return relatorioData
    } catch (error) {
        console.error("Erro na geração do relatório para download", error)
        throw error
    }
}

function iniciarDownload( dados, nomeDaTurma) {
    const nomeDoArquivo = nomeDaTurma + '.csv'
    const csv = converteArrayParaCsv(dados)
    console.log(csv)   
    const blob = new Blob([csv], { type: 'text/csv' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = nomeDoArquivo
    a.style.display = 'none'
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
}

function converteArrayParaCsv(dados) {
    const linhas = dados.map(obj => Object.values(obj).join(','))
    return [...linhas].join('\n')
}
