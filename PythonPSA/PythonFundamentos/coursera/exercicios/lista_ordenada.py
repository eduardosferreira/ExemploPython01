#coding:utf-8 
def ordenada(lista):
    fim = len(lista)
    for i in range (fim - 1):
        pos_menor = i
        for j in range (i + 1, fim):
            if lista[j] < lista[pos_menor]:
                return False
    return True

#numeros = [55,33,0,900,-432,10,77,123,11]
#print(ordenada(numeros))