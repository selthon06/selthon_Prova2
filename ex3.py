import random
precos = [random.randint(100, 500) for _ in range(1000)]

def aplicar_descontos(precos, *args):
    total = 0
    for preco in precos:
        novo_preco = preco
        for desc in args:
            if isinstance(desc, float) and 0 < desc < 1:
                novo_preco *= (1 - desc)
            elif isinstance(desc, int) or isinstance(desc, float):
                novo_preco -= desc
        total += max(novo_preco, 0)
    return f"Total a pagar: R$ {total:,.2f}".replace('.', ',') 


print(aplicar_descontos(precos, 0.10, 15))
