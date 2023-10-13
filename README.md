# FATEC-API-1-SEMESTRE

Trabalho de API do 1º semestre da FATEC.
### Tema
Desenvolver uma solução para a instituição de ensino PBLTex, especializada em cursos práticas de ensino aplicando PBL(Problem Based Learning), que consiste em construir um sistema de informação direcionado para a gestão e acompanhamento de scores de alunos.
### Objetivos 
  Desenvolvimento de uma solução computacional que exercite a capacidade de pesquisa e autodidaxia dos integrantes dos grupos, no que tange:
- A aplicação (no projeto) de técnicas de programação para a construção de algoritmos.
- O uso de uma ferramenta que possibilite um Ambiente de Desenvolvimento Integrado (IDE) para o desenvolvimento da solução computacional.
- O aprendizado e aplicação de uma ou mais linguagens de programação para concepção do projeto.
- O exercício do compromisso, responsabilidade e trabalho em equipe dos membros do Time (sucesso / fracasso de TODOS).

### Requisitos Funcionais
- O SI deve possuir um controle de Turmas.
- O SI deve possuir um controle de Grupos de Alunos.
- O SI deve permitir um controle de Alunos.
- O SI deve permitir a carga de Alunos.
- O SI deve permitir um controle dos Ciclos de Entrega.
- O SI deve permitir a carga de Scores parciais relacionados ao Ciclo de Entrega.
- O SI deve permitir a Configuração de parâmetros globais.
- O SI deve permitir a exportação de dados consolidados, computados e métricas inferidas.
- O SI deve prover visibilidades objetivas e diretas que possibilitem o acompanhamento dos cursos providos pela PBLTeX.

### Requisitos Não Funcionais
- Linguagem de programação Python e tecnologias relacionadas.
- Uso de bases de dados simples, dentre as opções: Arquivo(Text, CSV, Json ou outros formatos) ou ZODB.
- Sistema de controle de versão de código (Git)
- Documentações

### Documentação do projeto

Para acessar a documentação do projeto, fique a vontade para ver nosso site.

[Documentação FATEC API](https://github.com/ClaraSantosmf/FATEC-API-1S-DOCUMENTS)

#### Prazos

<table border="1 px">
    <tr>
        <th> Sprints </th>
        <th> Início </th>
        <th> Fim </th>
    </tr>
    <tr>
        <td> 1ª sprint </td>
        <td> 04/09 </td>
        <td> 24/09 </td>
    </tr>
    <tr>
        <td> 2ª sprint </td>
        <td> 25/09 </td>
        <td> 15/10 </td>
    </tr>
    <tr>
        <td> 3ª sprint </td>
        <td> 16/10 </td>
        <td> 05/11 </td>
    </tr>
    <tr>
        <td> 4ª sprint </td>
        <td> 06/11 </td>
        <td> 26/11 </td>
    </tr>
    <tr>
        <td> Feira de Soluções </td>
        <td> 12/12 </td>
        <td> 12/12 </td>
    </tr>

</table>

### Priorização das Sprints

O Kanbam utilizado possui quatro colunas. Backlog geral do projeto se encontra em aba de backlog. As tasks priorizada para a sprint que está ocorrendo na aba Priorizado. As task em execução estão na aba Coding, e as tasks já finalizadas na aba Done.

[Board Kanbam com a priorização](https://github.com/users/ClaraSantosmf/projects/5)

Ao abrir os cards do kanbam será possível ver a priorização no lado direito como um dos atributos dos cards, com as seguintes nomenclaturas.

Legenda Priorização:

<table border="1 px">
    <tr>
        <th> Tipo </th>
        <th> Representação </th>
    </tr>
    <tr>
        <td>Tarefas que entregarão maior valor de negócio </td>
        <td>🔴prioridade-máxima</td>
    </tr>
     <tr>
        <td>Tarefas que entregarão valor de negócio médio </td>
        <td>🟠prioridade-média</td>
    </tr>
     <tr>
        <td>Tarefas que entregarão valor baixo de negócio</td>
        <td>🟡prioridade-baixa</td>
    </tr>
</table>

Obs: Os cards na coluna "priorizado" são os cards escolhidos para serem feitos na próxima sprint.

[Aqui se encontra os detalhamentos dos épicos](https://clarasantosmf.github.io/FATEC-API-1S-DOCUMENTS/sprints/#epicos) que será desenvolvdo ao longo de todo o projeto.

Nos hiperlinks, você pode encontrar as tasks detalhadas da próxima sprint.


## Board de Produto

| Prioridade | Épicos planejados | UserStory | Sprint |
| ------------- | ------------- | ------------- | ------------- |
| Alta | [**Gerenciamento de Turmas:**](https://clarasantosmf.github.io/FATEC-API-1S-DOCUMENTS/sprints/#epico-2-gerenciamento-de-turmas_1) | Como administrador, quero realizar CRUD em relação às turmas| [#2]  |
| Alta | [**Global Settings**](https://clarasantosmf.github.io/FATEC-API-1S-DOCUMENTS/sprints/#epico-6-configuracoes-globais_1)  | Como administrador, quero realizar CRUD em relação ao Global Settings|[#2]  |
| Alta | [**Gerenciamento de Grupo**](https://clarasantosmf.github.io/FATEC-API-1S-DOCUMENTS/sprints/#epico-3-gerenciamento-de-grupos) | Como administrador, quero realizar o CRUD para grupos, organizando os alunos e facilitar a gestão. | [#3]  |
| Alta | [**Gerenciamento de Alunos**](https://clarasantosmf.github.io/FATEC-API-1S-DOCUMENTS/sprints/#epico-4-gerenciamento-de-alunos) | Como administrador, desejo realizar operações CRUD relacionadas aos alunos, no sistema. | [#3]  |
| Média | [**Gerenciamento de Ciclos de Entrega e Scores:**](https://clarasantosmf.github.io/FATEC-API-1S-DOCUMENTS/sprints/#epico-5-gerenciamento-de-ciclos-de-entrega-e-scores) | Como administrador, desejo ter a capacidade de criar e gerenciar ciclos de entrega e pontuações (scores) associados a esses ciclos para acompanhar o desempenho dos alunos. Sendo possível as operações do CRUD | [#4] |
| Média | [**Importação massiva de dados**](https://clarasantosmf.github.io/FATEC-API-1S-DOCUMENTS/sprints/#epico-7-carregamento-de-dados-massivo) | Como administrador, desejo importar dados em massa para o sistema a partir de arquivos externos, facilitando a entrada de informações de alunos, turmas e outros dados relacionados por meio de um CSV. | [#4] |
| Baixa | [**Visibilidade e Acompanhamento (relatório)**](https://clarasantosmf.github.io/FATEC-API-1S-DOCUMENTS/sprints/#epico-1-exportacao-de-dados) | Como administrador, desejo acessar relatórios que forneçam visibilidade sobre o desempenho dos alunos, as atividades da turma e outras métricas relevantes, a fim de tomar decisões informadas. Produzindo um PDF. | [#4] |
| Baixa | [**Carga massiva de Alunos**](https://clarasantosmf.github.io/FATEC-API-1S-DOCUMENTS/sprints/#epico-7-carregamento-de-dados-massivo) | Como administrador, desejo ter a capacidade de realizar a carga massiva de alunos no sistema, permitindo a inclusão rápida de um grande número de alunos de uma só vez por meio de CSV. | [#4] |


# Produto

### Tecnologias e Ferramentas Utilizadas

![alt text](/imgs_readme/tecnologias_api.png)

### Como configurar e rodar o projeto localmente

[Como rodar o projeto localmente](https://clarasantosmf.github.io/FATEC-API-1S-DOCUMENTS/biblioteca/#como-configurar-o-projeto)

### Wireframe do Produto

[Wireframe e fluxos do produto](https://drive.google.com/file/d/11kEv7yY0BUoWFASJIspfX-r-RI8AM4cm/view?usp=sharing)


### Equipe

| Integrantes | Redes Sociais |
|-------|--------|
|Caio Augusto Palma ![Static Badge](https://img.shields.io/badge/Dev-black)|<a href="https://github.com/caiopalma" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|Maria Clara Freitas Santos ![Static Badge](https://img.shields.io/badge/Scrum_master-pink)![Static Badge](https://img.shields.io/badge/Dev-black)|<a href="https://github.com/ClaraSantosmf" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|Danielle Mayumi Tamazato Santos ![Static Badge](https://img.shields.io/badge/Dev-black) |<a href="https://github.com/danitamazato" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|Eruano Rubens de ALmeida ![Static Badge](https://img.shields.io/badge/Dev-black)|<a href="www.github.com" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|Marília Borgo de Moraes ![Static Badge](https://img.shields.io/badge/Dev-black)|<a href="https://github.com/marilia-borgo" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|Mateus Soares ![Static Badge](https://img.shields.io/badge/Product_owner-blue)![Static Badge](https://img.shields.io/badge/Dev-black) |<a href="https://github.com/MateusMSoares" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|Ruth da Silva Mira ![Static Badge](https://img.shields.io/badge/Dev-black) |<a href="https://github.com/RuthMira" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|Sara Robert Nara ![Static Badge](https://img.shields.io/badge/Dev-black) |<a href="https://github.com/sararobertnahra" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
|William Gomes de Freitas ![Static Badge](https://img.shields.io/badge/Dev-black) |<a href="https://github.com/willigfreitas" target="_blank"><img src="https://img.shields.io/badge/-black?style=social&logo=github&label=github&color=black" target="_blank"></a>|
