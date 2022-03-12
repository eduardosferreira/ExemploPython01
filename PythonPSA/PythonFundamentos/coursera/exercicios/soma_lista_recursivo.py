#coding:utf-8 
def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    return lista[0] + soma_lista(lista[1:])

#a = [1,2,3,4]
#print(soma_lista(a))