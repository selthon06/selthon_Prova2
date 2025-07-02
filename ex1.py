def criar_dicionario(admin, operacional, tecnico):
    return {
        'Administrativo': tuple(admin),
        'Operacional': tuple(operacional),
        'Técnico': tuple(tecnico)
    }

def setores_com_mais_de_dois(dicionario):
    for setor, nomes in dicionario.items():
        if len(nomes) > 2:
            print(f"{setor}: {len(nomes)} participantes")

def exibir_nomes_ordenados(dicionario):
    todos_nomes = []
    for nomes in dicionario.values():
        todos_nomes.extend(nomes)
    todos_nomes.sort()
    print("Nomes em ordem alfabética:")
    for nome in todos_nomes:
        print(nome)

admin = ['Ana', 'Carlos', 'Bia']
operacional = ['selthon', 'Rita']
tecnico = ['Lucas', 'Tiago', 'Fernanda', 'Rafael']

d = criar_dicionario(admin, operacional, tecnico)
setores_com_mais_de_dois(d)
exibir_nomes_ordenados(d)
