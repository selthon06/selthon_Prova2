empresa = {
    'nome': 'João',
    'cargo': 'CEO',
    'salario': 10000.0,
    'subordinados': [
        {
            'nome': 'Maria',
            'cargo': 'Gerente',
            'salario': 7000.0,
            'subordinados': [
                {
                    'nome': 'Carlos',
                    'cargo': 'Analista',
                    'salario': 4000.0,
                    'subordinados': []
                }
            ]
        },
        {
            'nome': 'Ana',
            'cargo': 'Coordenadora',
            'salario': 6000.0,
            'subordinados': []
        }
    ]
}

def contar_funcionarios(funcionario):
    total = 1 
    for sub in funcionario['subordinados']:
        total += contar_funcionarios(sub)
    return total

def somar_salarios(funcionario):
    total = funcionario['salario']
    for sub in funcionario['subordinados']:
        total += somar_salarios(sub)
    return total

def profundidade_maxima(funcionario):
    if not funcionario['subordinados']:
        return 1
    profundidades = [profundidade_maxima(sub) for sub in funcionario['subordinados']]
    return 1 + max(profundidades)

print("Total de funcionários:", contar_funcionarios(empresa))
print("Folha salarial total: R$", somar_salarios(empresa))
print("Profundidade máxima da hierarquia:", profundidade_maxima(empresa))
