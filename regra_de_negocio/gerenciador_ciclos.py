from regra_de_negocio.global_settings import obter_quantidade_sprint

def criar_ciclos_padrao():
    ciclos = {}
    quantidade_sprint = obter_quantidade_sprint()
    for i in range(int(quantidade_sprint) if quantidade_sprint else 4):
        j = i + 1
        ciclos[str(j)] = {"peso":float(j)}
    return ciclos