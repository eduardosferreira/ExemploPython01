#coding:utf-8
"""
#Programa
    Remove repetidos
"""

def remove_repetidos (p_ob_lst):
    return fnc_remove_repetidos(p_ob_lst=p_ob_lst)

def fnc_remove_repetidos(p_ob_lst):
    """
    Funcao remove repetidos
    """
    ob_lst = []
    if isinstance(p_ob_lst, list):
        ob_lst = list(set(p_ob_lst))
        ob_lst.sort()
    
    return ob_lst
    
def main():
    """
    Funcao principal
    """
    # criacao lista de vazia
    ob_lst = []
 
    # numero de elementos
    nr_qtde_elementos = int(input("Entra com numero de elementos : "))
 
    if nr_qtde_elementos <= 0:
        return
        
    # interacao
    for nr_idx in range(0, nr_qtde_elementos):
        nr_elemento = int(input())
        ob_lst.append(nr_elemento) # adicao de elementos
     
    print("Digitados ", str(ob_lst))
    
    ob_lst = fnc_remove_repetidos(p_ob_lst=ob_lst)
    
    print("Acionado a funcao ", str(ob_lst))
    
    
if __name__ == "__main__" :
    """
    Ponto de inicio
    """

    # Aciona a funcao principal
    main()
        
#Fim do programa
