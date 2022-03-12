#Calculadora

"""
funcao Somar
"""
somaF = lambda x,y: x+y

"""
funcao Subtratir
"""
subtrairF = lambda x,y: x-y

"""
funcao Multiplicar
"""
multiplicarF = lambda x,y: x*y

"""
funcao Dividir
"""
dividirF = lambda x,y: x/y

def calculadora():
    while True:
        print()
        print (str (" Python Calculadora ").center (100, "#"))
        print ("\nInforme a operação desejada :")
        print (" 1 para Soma ", end=" - > ")
        print (" 2 para Substrair ", end=" - > ")
        print (" 3 para Multiplicar ", end=" - > ")
        print (" 4 para Dividir ", end=" -> ")
        print (" 0 ou outra tecla para Sair ")
        l_operacao = str (input ("\nOperação: ")).strip ( )
        if (l_operacao not in ("1","2","3","4")):
            print ("Obrigado")
            break
        else:
           try:
               l_numero1 = str (input ("\nDigite primeiro número: ")).strip( )
               l_numero2 = str (input ("\nDigite segundo  número: ")).strip( )
               l_resultado = float(0)
               print()
               if l_operacao == "1":
                   print("Soma: ".rjust(15,"*"),end=' ')
                   l_resultado = somaF(float(l_numero1),float(l_numero2))
               elif l_operacao == "2":
                   print ("Subtrair: ".rjust (15, "*"), end=' ')
                   l_resultado = subtrairF(float(l_numero1),float(l_numero2))
               elif l_operacao == "3":
                   print ("Multiplicar: ".rjust (15, "*"), end=' ')
                   l_resultado = multiplicarF(float(l_numero1),float(l_numero2))
               elif l_operacao == "4":
                   print ("Dividir: ".rjust (15, "*"), end=' ')
                   l_resultado = dividirF(float(l_numero1),float(l_numero2))
               print("%.2f" %(l_resultado))
           except:
               print("Falha na operação!")


def main():
    calculadora()


if __name__ == '__main__':
    main();