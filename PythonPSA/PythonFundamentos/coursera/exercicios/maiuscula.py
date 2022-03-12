#coding:utf-8
"""
#Programa
    maiúscula
    
Exercício 1: Letras maiúsculas
Escreva a função maiusculas(frase) que recebe uma frase (uma string) como parâmetro e devolve uma string 
com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.

Para resolver este exercício, pode ser útil verificar uma tabela ASCII, que contém os valores de cada caractere. 
Ver https://pt.wikipedia.org/wiki/ASCII

Note que para simplificar a solução do exercício, as frases passadas para a sua função não possuirão caracteres
 que não estejam presentes na tabela ASCII apresentada, como ç, á, É, ã, etc.

Dica: Os valores apresentados na tabela são os mesmos devolvidos pela função ord apresentada nas aulas.

Exemplos:    

maiusculas('Programamos em python 2?')
# deve devolver 'P'

maiusculas('Programamos em Python 3.')
# deve devolver 'PP'

maiusculas('PrOgRaMaMoS em python!')
# deve devolver 'PORMMS'

"""

import string 

def maiusculas(parametro):
    return fnc_maiusculas(parametro)

def fnc_maiusculas(p_cc_dados):
    ''' 
    (str)
    Funcao verifica quais são os dados maiusculas
    '''
    
    cc_dados = ""
    
    cc_lista = str(p_cc_dados)
    
    try:

        for dado in cc_lista:
            if dado in string.ascii_uppercase:
                cc_dados += dado            
                
    
    except:
    
        pass
    
    return cc_dados

def main():
    """
    Funcao principal
    """
    cc_dado = input("Digita os dados: ")
    
    print(fnc_maiusculas(cc_dado))
    
if __name__ == "__main__" :
    """
    Ponto de inicio
    """

    # Aciona a funcao principal
    main()
        
#Fim do programa
