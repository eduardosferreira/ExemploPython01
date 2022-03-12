#coding:utf-8 
def bubble_sort(lista):
    for passnum in range(len(lista)-1,0,-1):
        for i in range(passnum):
            if lista[i]>lista[i+1]:
                #temp = lista[i]
                #lista[i] = lista[i+1]
                #lista[i+1] = temp
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                print(lista)
    return lista

#bubble_sort([1, 5, 3, 4, 2, 0])
#bubble_sort([5, 1, 4, 2])