#coding:utf-8
"""
#Programa
    Numero primos
"""

def fnc_primo(p_nr):
    """
    Funcao verifica numero primo
    """
    try:
    
        nr_dado = int(p_nr)
    
        nr_aux = 2

        while nr_aux * nr_aux <= nr_dado:
            if (nr_dado % nr_aux) == 0:
                return False
            nr_aux += 1

        return True
    
    except:
    
        return False

def fnc_maior_primo(p_nr):
    """
    Funcao verifica maior numero primo
    """
    try:
    
        nr_dado = int(p_nr)
        
        if nr_dado < 2:
            return None
    
        nr_aux = nr_dado
    
        nr_maior = 0

        while nr_aux >= 2:
            if fnc_primo(nr_aux):
                return nr_aux
            nr_aux -= 1

        return 2

    except:
        return None
        
def fnc_lista_primo(p_nr):
    """
    Funcao verifica lista numero primo
    """

    ls_primo = []
    
    try:
    
        nr_dado = int(p_nr)
    
        if nr_dado < 2:
            return ls_primo
    
        nr_aux = nr_dado
    
        while nr_aux >= 2:
            if fnc_primo(nr_aux):
                ls_primo.append(nr_aux)
            nr_aux -= 1

        return ls_primo

    except:
        return ls_primo
    
def main():
    """
    Funcao principal
    """
    cc_dado = input("Verificar numeros primos ate: ")
    
    if fnc_maior_primo(cc_dado) is not None:
        
        for dado in fnc_lista_primo(cc_dado):
            print(" - primo : ", dado)
    else:
        print("Dado invalido! ")
    
if __name__ == "__main__" :
    """
    Ponto de inicio
    """

    # Aciona a funcao principal
    main()
        
#Fim do programa
