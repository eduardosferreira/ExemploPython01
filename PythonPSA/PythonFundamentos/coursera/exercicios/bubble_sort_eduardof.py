#coding:utf-8 
def bubble_sort(lista):
    loop = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True

        for i in range(loop):
            if lista[i] > lista[i+1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                ordenado = False
        print(lista)
    return lista


#bubble_sort([5, 1, 4, 2])
#bubble_sort([1, 5, 3, 4, 2, 0])