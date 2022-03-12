#coding:utf-8
"""
#Programa 
 Matriz   
"""

def cria_matriz(num_linhas,num_colunas,valor=0):
    '''
    (int,int,float) ->  fnc_matriz (lista de listas)
    Funcao que cria uma matriz com numero de linhas e colunas
    de acordo com um valor
    '''
    return fnc_matriz(p_nr_linhas=num_linhas,p_nr_colunas=num_colunas,p_nr_valor=valor)

def fnc_matriz(p_nr_linhas=0,p_nr_colunas=0,p_nr_valor=-1):
    # criacao variaveis
    ob_matriz = [] # lista vazia
    nr_linhas = int(p_nr_linhas)
    nr_colunas = int(p_nr_colunas)
    nr_valor = float(p_nr_valor)
    bl_valida = True
    if nr_linhas > 0:
        bl_valida = False    
                
    while bl_valida:
        try:
            nr_linhas = int(input("Entra com quantidade de linhas: "))
        except:
            nr_linhas = 0        
        if nr_linhas <= 0:    
            print("Entrada invalida! ...")
        else:
            bl_valida = False
            
    bl_valida = True
    if nr_colunas > 0:
        bl_valida = False    
    
    while bl_valida:
        try:
            nr_colunas = int(input("Entra com quantidade de colunas: "))
        except:
            nr_colunas = 0        
        if nr_colunas <= 0:    
            print("Entrada invalida! ...")
        else:
            bl_valida = False
    
    bl_valida_aux = True
    bl_valida = True
    if nr_valor >= 0: 
        bl_valida = False    
        bl_valida_aux = False
    
    for nr_linha in range(nr_linhas):
        ob_linha = [] # lista vazia da linha
        for nr_coluna in range(nr_colunas):
            if bl_valida_aux:
                bl_valida = True
                while bl_valida:
                    try:
                        nr_valor = int(input("Entra com valores [ " + str(nr_linha) +  " ] [ " + str(nr_coluna) +  " ] : "))
                        ob_linha.append(nr_valor)
                        bl_valida = False
                    except:
                        print("Entrada invalida! ...")
                            
            else:
                ob_linha.append(nr_valor)                
        ob_matriz.append(ob_linha)        
    
    return ob_matriz
    
def fnc_remove_repetidos(p_ob_lst):
    '''
    (lista) - > lista
    Funcao remove repetidos
    '''
    ob_lst = []
    if isinstance(p_ob_lst, list):
        ob_lst = list(set(p_ob_lst))
        ob_lst.sort()
    
    return ob_lst

def fnc_cria_array():
    '''
    Funcao cria array
    '''
    # criacao variaveis
    ob_lst = []
    nr_qtde_elementos = 0
    nr_elemento = 0
    bl_valida_entrada = True
    
    # numero de elementos
    while bl_valida_entrada:
        try:
            nr_qtde_elementos = int(input("Entra com numero de elementos : "))
            bl_valida_entrada = False
        except:
            print("Entrada incorreto!")
            
    if nr_qtde_elementos <= 0:
        print("Entrada menor que o permitido! FIM ...")
        return
         
    # interacao
    for nr_idx in range(0, nr_qtde_elementos):
        bl_valida_entrada = True
        while bl_valida_entrada:
            try:
                nr_elemento = int(input("Elemento: "))
                ob_lst.append(nr_elemento) # adicao de elementos
                bl_valida_entrada = False
            except:
                print("Entrada incorreto!")            
    
    print("Lista ...")
        
    print("Antes ... ", str(ob_lst))
    
    print("Remove duplicados ... ")
    ob_lst = fnc_remove_repetidos(p_ob_lst=ob_lst)
    
    print("Depois ... ", str(ob_lst))

def fnc_imprimir_matriz(p_ob_matriz):
    '''
    Funcao imprimir matriz
    '''
    print("*"*10)
    print("")
    if isinstance(p_ob_matriz, list):
        if isinstance(p_ob_matriz[0], list):
            if len(p_ob_matriz) > 0:    
                print("[")
                for nr_linha in range(len(p_ob_matriz)):
                    if len(p_ob_matriz[nr_linha]) > 0:        
                        print(" " + "[",end='')
                        for nr_coluna in range(len(p_ob_matriz[nr_linha])):
                            if nr_coluna == len(p_ob_matriz[nr_linha])-1:
                                print(str(p_ob_matriz[nr_linha][nr_coluna]),end='')
                            else:
                                print(str(p_ob_matriz[nr_linha][nr_coluna]),end=',')
                        print("]")
                print("]") 
            else:
                print("Não possui dados de uma matriz!")
        else:
            print("Não e uma matriz! Não tem colunas ... ")
    else:
        print("Não e uma matriz! Não tem linhas ... " )
        
    print("")
    print("*"*10)
    
def fnc_leitura_matriz():
    '''
    Funcao leitura matriz
    '''
    ob_matriz = fnc_matriz()    
    fnc_imprimir_matriz(ob_matriz)
    
def main():
    '''
    Funcao principal
    '''
    fnc_leitura_matriz()
       
if __name__ == "__main__" :
   """
   Ponto de inicio
   """

   # Aciona a funcao principal
   main()
        
#Fim do programa
