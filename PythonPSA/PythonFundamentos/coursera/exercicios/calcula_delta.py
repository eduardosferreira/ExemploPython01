#coding:utf-8
"""
#Programa, raiz de uma equação do segundo grau
#
#
"""

from math import sqrt as raiz_quadrada


def fnc_retorna_valor(p_str_valor):
    """
    Funcao de retorno de valor
    """
    try:
        nr_valor = float(input("Informe o valor " + str(p_str_valor)+ " : "))
        return nr_valor
    except Exception as e:
        print("*** Erro na entrada de dados *** " + str(e))
        return None    


def fnc_raiz(p_nr_a, p_nr_b, p_nr_d):
    """
    Funcao de calculo de raiz
    """

    if p_nr_a == 0:
        return 0
    
    return (-1*p_nr_b + raiz_quadrada(p_nr_d))/2*p_nr_a


def fnc_delta(p_nr_a, p_nr_b, p_nr_c):
    """
    Funcao de calculo de delta
    """

    return p_nr_b**2 - 4 * p_nr_a * p_nr_c


def fnc_entrada_dados():
    """
    Funcao para validar a entrada de dados
    """

    global gv_nr_a
    global gv_nr_b
    global gv_nr_c
    
    gv_nr_a = fnc_retorna_valor("a")
    if gv_nr_a is None:
        return False

    gv_nr_b = fnc_retorna_valor("b")
    if gv_nr_b is None:
        return False

    gv_nr_c = fnc_retorna_valor("c")
    if gv_nr_c is None:
        return False
    
    return True    


def main():
    """
    Funcao principal
    """

    global gv_nr_a
    global gv_nr_b
    global gv_nr_c
    global gv_nr_d

    # Valida a entrada de dados
    if fnc_entrada_dados():
        # Calcula delta
        gv_nr_d = fnc_delta(p_nr_a=gv_nr_a, p_nr_b=gv_nr_b, p_nr_c=gv_nr_c)

        # imprimi as raizes 
        if gv_nr_d < 0:
            print("A equação não possui raizes reais." + " - > Delta : " + str(gv_nr_d))
        elif gv_nr_d == 0:
            print("A equacao possui apenas uma raiz que e ",str(fnc_raiz(p_nr_a=gv_nr_a, p_nr_b=gv_nr_b, p_nr_d=gv_nr_d)))
        elif delta > 0:
            nr_raiz1 = fnc_raiz(p_nr_a=gv_nr_a, p_nr_b=gv_nr_b, p_nr_d=gv_nr_d)
            nr_raiz2 = fnc_raiz(p_nr_a=gv_nr_a, p_nr_b=gv_nr_b, p_nr_d=gv_nr_d)
            print("As raizes da equacao sao ",nr_raiz1, "e",nr_raiz2)
            
"""
Ponto de partida
"""
if __name__ == "__main__" :

    # Variaveis globais para validacao
    gv_nr_a = float(0)
    gv_nr_b = float(0)
    gv_nr_c = float(0)
    gv_nr_d = float(0)

    # Aciona a funcao principal
    main()
        
#Fim do programa
