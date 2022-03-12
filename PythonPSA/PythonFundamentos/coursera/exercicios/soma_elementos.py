#coding:utf-8
"""
#Programa
    Soma elementos
"""

def soma_elementos  (p_ob_lst):
    return fnc_soma_elementos (p_ob_lst=p_ob_lst)

def fnc_soma_elementos (p_ob_lst):
    """
    Funcao soma elementos
    """
    nr_elemento = 0
    if isinstance(p_ob_lst, list):
        nr_elemento = sum(p_ob_lst)
    
    return nr_elemento
    
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
    
    print("Acionado a funcao ", str(fnc_soma_elementos (p_ob_lst=ob_lst)))
        
if __name__ == "__main__" :
    """
    Ponto de inicio
    """
    # Aciona a funcao principal
    main()
        
#Fim do programa
