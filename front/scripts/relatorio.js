async function carregarSelectTurma(graficoAluno){
    let selectTurma = document.getElementById('selectTurma')
    
    const turmas = {
        '1':{'nome':'ADS'},
        '2':{'nome':'Banco de Dados'},
        '3':{'nome':'Logistica'}
    }

    for( chave in turmas ){
        const novaOpcao = document.createElement('option');
        novaOpcao.value = chave
        novaOpcao.text = `${turmas[chave]['nome']}`
        selectTurma.appendChild(novaOpcao)
    }

    selectTurma.addEventListener(
        'change',  
        async () => {
            const idTurma = selectTurma.value
            await graficoAluno.setIdTurma(idTurma)
        }
    )
}

class GraficoAluno {
    constructor(idTurma){
        this.grafico = null
        this.idCanvas = 'graficoAluno'
        this.idTurma = idTurma
    }

    async setIdTurma(idTurma){
        this.idTurma = idTurma
        await this.plotarGrafico()
    }

    async carregarDados(idTurma){
        const dados = {
            labels: [],
            data: []
        }
            if( idTurma == '' || idTurma == null ){
                return dados
        }
        const res = await fetch(`http://127.0.0.1:8080/api/v1/relatorios/grafico_alunos/${idTurma}`)
        const dados_aluno = await res.json()

        for(let id_aluno in dados_aluno){
            const aluno = dados_aluno[id_aluno]
            dados.labels.push(aluno.nome)
            dados.data.push(aluno.fee)
        }
        return dados
    }

    async obterConfiguracao(){
        const dados = await this.carregarDados(this.idTurma)
        const configuracao = {
            type: 'bar',
            data: {
                labels: dados.labels,
                datasets: [{
                    label: 'FEE',
                    data: dados.data,
                    borderWidth: 1
                }]  
            },
            options: {
                scales: {
                    y: {
                        min:0.0,
                        max:10.0
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Gráfico: FEE x Aluno'
                    }
                }
            }
        }
        return configuracao
    }

    async plotarGrafico() {
        if( this.grafico != null ){
            this.grafico.destroy()
        }
        const canvas = await this.getCanvas();
        const configuracao = await this.obterConfiguracao()
        this.grafico = await new Chart(canvas, configuracao);
    }   
    async getCanvas(){
        return document.getElementById(this.idCanvas)
    }
}

class GraficoTurma {
    constructor(){
        this.grafico = null
        this.idCanvas = 'graficoTurma'
    }

    async carregarDados(){
        const dados = {
            labels: [],
            data: []
        }
        const res = await fetch('http://127.0.0.1:8080/api/v1/relatorios/grafico_turmas')
        const dados_turma = await res.json()
        for(let id_turma in dados_turma){
            const turma = dados_turma[id_turma]
            dados.labels.push(turma.nome)
            dados.data.push(turma.fee)
        }
        return dados
    }

    async obterConfiguracao(){  
        const dados = await this.carregarDados()
        const configuracao = {
            type: 'bar',
            data: {
                labels: dados.labels,
                datasets: [{
                    label: 'FEE',
                    data: dados.data,
                    borderWidth: 1
                }]  
            },
            options: {
                scales: {
                    y: {
                        min: 0.0,
                        max: 10.0
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Gráfico: FEE x Turma'
                    }
                }
            }
        }
        return configuracao
    }
    
    async plotarGrafico() {
        if( this.grafico != null ){
            this.grafico.destroy()
        }
        const canvas = await this.getCanvas();
        const configuracao = await this.obterConfiguracao()
        this.grafico = new Chart(canvas, configuracao);
    }

    async getCanvas(){
        return document.getElementById(this.idCanvas)
    }
}

let graficoAluno = new GraficoAluno('')
graficoAluno.plotarGrafico()

let graficoTurma = new GraficoTurma()
graficoTurma.plotarGrafico()

carregarSelectTurma(graficoAluno)