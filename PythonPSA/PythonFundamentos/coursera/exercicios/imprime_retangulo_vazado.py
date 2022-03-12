#coding:utf-8
"""
#Programa
Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres 
que não estiverem na borda do retângulo sejam espaços.
"""

def main():
    """
    Funcao principal
    """
    
    nr_largura = nr_l  = 1
    
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
            if ( (nr_l == 1 or nr_l == nr_largura) or (nr_a == 1 or nr_a == nr_altura) ):
                print("#",end='')
            else:
                print(" ",end='')
            nr_l += 1    
        
        print()    
        nr_a += 1
        nr_l = 1
    
if __name__ == "__main__" :
    """
    Ponto de inicio
    """

    # Aciona a funcao principal
    main()
        
#Fim do programa
