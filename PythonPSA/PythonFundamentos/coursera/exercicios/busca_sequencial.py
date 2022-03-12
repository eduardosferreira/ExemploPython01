def busca(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False

#numeros = [55,33,0,900,-432,10,77,123,11]
#print(busca(numeros,12))