valores = ["A", "B", "C", "D", "E"]
indice = 0

def round_robin_selection(lista: list, ultimo_valor: str):
    if not lista:
        return None
    if not ultimo_valor:
        return lista[0]
    indice_atual = lista.index(ultimo_valor)
    prox_indice = (indice_atual + 1) % len(lista)

    return lista[prox_indice]
    
    

if __name__ == '__main__':
    valor = None

    for _ in range(10):
        valor = round_robin_selection(valores, valor)
        print(valor)