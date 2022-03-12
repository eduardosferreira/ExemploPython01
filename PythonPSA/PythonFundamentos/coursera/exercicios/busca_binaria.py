#coding:utf-8 
def busca(lista,elemento):
    primeiro = 0
    ultimo = len(lista)-1
    encontrado = False

    while primeiro <= ultimo and not encontrado:
        meio = (primeiro + ultimo) // 2
        print(meio)
        if lista[meio] == elemento:
             return meio
        elif elemento < lista[meio]:
            ultimo = meio - 1
        else:
            primeiro = meio + 1

    return encontrado

#busca(['a', 'e', 'i'], 'e')