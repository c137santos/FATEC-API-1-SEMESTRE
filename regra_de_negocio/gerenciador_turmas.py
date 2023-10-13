import json


# Esta função busca informações sobre as turmas a partir de um arquivo JSON e as retorna
def busca_turmas():
    with open("dados/turmas.json", "r", encoding="utf-8") as f:
        turmas_data = json.load(f)
    return turmas_data


def busca_grupos():
    with open("dados/grupos.json", "r", encoding="utf-8") as f:
        grupos_Data = json.load(f)
    return grupos_Data

# Função para criar uma nova turma
def criacao_turma(dados_nova_turma):
    body_tratado = json.loads(dados_nova_turma)
    turmas = busca_turmas()
    grupos = busca_grupos()

    turma_novo_id = str(len(turmas) + 1)

    nova_turma = {
        "nome": body_tratado["nome"],  # Acesse a propriedade "nome" do corpo
        "professor": body_tratado["professor"],  # Acesse a propriedade "professor" do corpo
        "data_de_inicio": body_tratado["dataInicio"]  # Acesse a propriedade "dataInicio" do corpo
    }
    turmas[turma_novo_id] = nova_turma
    turma_nome = turmas[turma_novo_id]["nome"]
    resposta = {
    "mensagem": f"Criação da turma {turma_nome.capitalize()} realizada com sucesso!",
    "detalhes": []
    }

    if len(body_tratado["grupos"]) >= 1:
        for idGrupo in body_tratado["grupos"]:
            idGrupo = str(idGrupo) #transforma o inteiro da lista em str para comparar com as chaves
            print(f"ID do grupo a ser atualizado: {idGrupo}")
            # Verifique se o ID do grupo existe nos grupos
            if idGrupo in grupos:
                print(f"Atualizando grupo {idGrupo} para turma {turma_novo_id}")
                grupo_Nome = grupos[idGrupo]["nome"]
                grupos[idGrupo]["turma"] = int(turma_novo_id)  # Atualize a propriedade "turma" com um valor inteiro
                resposta["detalhes"].append(f"Adicionado o grupo {grupo_Nome.capitalize()} a turma {turma_nome.capitalize()}")
            else:
                resposta["detalhes"].append(f"id {grupo_Nome.capitalize()} não encontrado nos grupos")

            
    # Salve as alterações nos arquivos JSON
    salvar_turmas(turmas)
    salvar_grupos(grupos)
    return resposta

# Função para salvar turmas em um arquivo JSON
def salvar_turmas(turmas):
    with open("dados/turmas.json", "w", encoding="utf-8") as f:
        json.dump(turmas, f, indent=4)

# Função para salvar grupos em um arquivo JSON
def salvar_grupos(grupos):
    with open("dados/grupos.json", "w", encoding="utf-8") as f:
        json.dump(grupos, f, indent=4)
