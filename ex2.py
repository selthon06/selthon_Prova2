alunos = {
    'Ana': [-3],
    'Selthon': [-4],
    'Caio': [2],
    'Léo': [3],
    'Nana': [7],
    'digo': [4],
    'Laura': [2],
    'Paulo': [6]
}

aprovados = []

for nome, presencas in alunos.items():
    taxa_presenca = sum(presencas) / len(presencas)
    if taxa_presenca >= 3:
        aprovados.append(nome)

print("- ativo:", aprovados)
