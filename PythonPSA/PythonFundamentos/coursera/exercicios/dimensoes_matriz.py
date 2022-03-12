#coding:utf-8
"""
#Programa
Dimensoes matriz
"""

def dimensoes(minha_matriz):
   
    nr_linha = 0
    nr_coluna = 0

    if isinstance(minha_matriz, list):
        nr_linha = len(minha_matriz)
        if isinstance(minha_matriz[0], list):
            nr_coluna = len(minha_matriz[0])
    
    return str(nr_linha)+"X"+str(nr_coluna)

def imprime_matriz(minha_matriz):
    return dimensoes(minha_matriz)

def dimensoes_matriz(minha_matriz):
    return dimensoes(minha_matriz)


#Fim do programa
