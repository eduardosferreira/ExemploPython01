#coding:utf-8
"""
#Programa 
 Soma Matrizes   
"""
import Matriz # importa o arquivo Matriz.py que foi criado

def soma_matrizes(matriz_a, matriz_b):
    return fnc_soma_matrizes(p_ob_matriz_a=matriz_a, \
                             p_ob_matriz_b=matriz_b)

def fnc_soma_matrizes(p_ob_matriz_a, p_ob_matriz_b):
    ob_matriz_c = []
    nr_linhas = 0
    nr_colunas = 0
    
    if isinstance(p_ob_matriz_a, list) \
    and isinstance(p_ob_matriz_b, list):
        nr_linhas = len(p_ob_matriz_a)
        if nr_linhas != len(p_ob_matriz_b):
            return ob_matriz_c
            
        if isinstance(p_ob_matriz_a[0], list) \
        and isinstance(p_ob_matriz_b[0], list):
            nr_colunas = len(p_ob_matriz_a[0])
            if nr_colunas != len(p_ob_matriz_b[0]):
                return ob_matriz_c
            
    
    if nr_linhas > 0 \
    and nr_colunas > 0:
    
        ob_matriz_c = Matriz.cria_matriz(num_linhas=nr_linhas,num_colunas=nr_colunas)
    
        for nr_linha in range(nr_linhas):
            for nr_coluna in range(nr_colunas):    
                ob_matriz_c[nr_linha][nr_coluna] = \
                p_ob_matriz_a[nr_linha][nr_coluna] + \
                p_ob_matriz_b[nr_linha][nr_coluna]
                
    return ob_matriz_c

def fnc_multiplica_matrizes(p_ob_matriz_a, p_ob_matriz_b):
    ob_matriz_c = []
    nr_linhas_a = nr_colunas_a  = 0 
    nr_linhas_b = nr_colunas_b  = 0 
    
    if isinstance(p_ob_matriz_a, list):
        nr_linhas_a = len(p_ob_matriz_a)
        if isinstance(p_ob_matriz_a[0], list):
            nr_colunas_a = len(p_ob_matriz_a[0])
    
    if isinstance(p_ob_matriz_b, list):
        nr_linhas_b = len(p_ob_matriz_b)
        if isinstance(p_ob_matriz_b[0], list):
            nr_colunas_b = len(p_ob_matriz_b[0])
            
    
    if nr_linhas_a > 0 \
    and nr_colunas_a > 0 \
    and nr_linhas_b > 0 \
    and nr_colunas_b > 0:
            
        assert nr_linhas_a == nr_colunas_b
    
        assert nr_linhas_b == nr_colunas_a
    
        ob_matriz_c = Matriz.cria_matriz(num_linhas=nr_linhas_a,num_colunas=nr_colunas_b)
    
        for nr_linha in range(nr_linhas_a):
            for nr_coluna in range(nr_colunas_b):
                for nr_aux in range(nr_colunas_a):
                    ob_matriz_c[nr_linha][nr_coluna] += \
                    p_ob_matriz_a[nr_linha][nr_aux] * \
                    p_ob_matriz_b[nr_aux][nr_coluna]
                
    return ob_matriz_c


    
def fnc_leitura_matriz():
    '''
    Funcao leitura matriz
    '''
    
    print("Matriz A")
    ob_matriz_a = Matriz.fnc_matriz()
    
    print("Matriz B")
    ob_matriz_b = Matriz.fnc_matriz()
    
    print("Matriz C")
    nr_opcao = input("Encolha a opção [1] SOMA | [2] MULTIPLICAO : ")
    if nr_opcao.strip() == "1":
        ob_matriz_C = fnc_soma_matrizes(ob_matriz_a,ob_matriz_b)
        Matriz.fnc_imprimir_matriz(ob_matriz_C)
    else:
        ob_matriz_C = fnc_multiplica_matrizes(ob_matriz_a,ob_matriz_b)
        Matriz.fnc_imprimir_matriz(ob_matriz_C)
    
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