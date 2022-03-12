#coding:utf-8
"""
#Programa
Dimensoes matriz
"""

def soma_matrizes(m1,m2):
    
    ob_matriz = []
    ds_lst_1 = str(fnc_dimensoes_matriz(m1))
    ds_lst_2 = str(fnc_dimensoes_matriz(m2))
    
    if ds_lst_1 == ds_lst_2:
        if isinstance(m1, list) \
        and isinstance(m2, list):
            if len(m1) > 0:    
                for nr_linha in range(len(m1)):
                    ob_linha = [] # lista vazia da linha
                    if len(m1[nr_linha]) > 0:        
                        for nr_coluna in range(len(m1[nr_linha])):
                            ob_linha.append(m1[nr_linha][nr_coluna]+m2[nr_linha][nr_coluna])
                    ob_matriz.append(ob_linha)
                return ob_matriz
            else:
                return False
                
        else:
            return False
    
    else:
        return False
    
def fnc_dimensoes_matriz(p_ob_lst):
    '''
    (lista) - > imprimi dimensoes
    Funcao dimensoes aonde recebe uma matriz
    '''

    nr_linha = 0
    nr_coluna = 0

    if isinstance(p_ob_lst, list):
        nr_linha = len(p_ob_lst)
        if isinstance(p_ob_lst[0], list):
            nr_coluna = len(p_ob_lst[0])
    
    return str(nr_linha)+"X"+str(nr_coluna)

#Fim do programa
