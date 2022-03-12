#coding:utf-8   
def encontra_impares(lista):
    if not lista:
        return []
    if lista[0] % 2 == 1:
        return [lista[0]] + encontra_impares(lista[1:])
    return encontra_impares(lista[1:])

#a = [1,2,3,4]
#print(encontra_impares(a))