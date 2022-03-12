#coding:utf-8
"""
#Programa
Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes 
à largura e à altura de um retângulo, respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), 
uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.
"""

def main():
    """
    Funcao principal
    """
    
    nr_largura = nr_l = 1
    
    nr_altura = nr_a = 1
    
    bl_valido = False

    while not bl_valido:   
    
        try:
    
            nr_largura = int(input('digite a largura: '))
            
            nr_altura = int(input('digite a altura: '))
   
            if nr_largura > 0 and nr_altura > 0:
                bl_valido = True
                
            else:
                print('\nEscolha inválida! Tente de novo.\n')
        
        except:
        
            print('\nEscolha inválida! Tente de novo.\n')
            
    while nr_a <= nr_altura:
        while nr_l <= nr_largura:
            print("#",end='')
            if nr_l == nr_largura:
                print()
            nr_l += 1
            
        nr_a += 1
        nr_l = 1
    

if __name__ == "__main__" :
    """
    Ponto de inicio
    """

    # Aciona a funcao principal
    main()
        
#Fim do programa
