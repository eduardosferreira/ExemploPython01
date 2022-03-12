#coding:utf-8
"""
#Programa
    Menor nome
    
Exercício 2: Menor nome
Como pedido no primeiro vídeo desta semana, escreva uma função menor_nome(nomes) 
que recebe uma lista de strings com nome de pessoas como parâmetro e devolve o nome mais curto presente na lista.

A função deve ignorar espaços antes e depois do nome e deve devolver o menor nome presente na lista. Este nome deve ser devolvido com a primeira letra maiúscula e seus demais caracteres minúsculos, independente de como tenha sido apresentado na lista passada para a função.

Quando houver mais de um nome com o menor comprimento dentre os nomes na lista, a função deve devolver o primeiro nome com o menor comprimento presente na lista.

Exemplos:

"""

def menor_nome(parametro):
    return fnc_menor_nome(parametro)

def fnc_menor_nome(p_cc_dados):
    ''' 
    (str)
    Funcao verifica quais são os dados maiusculas
    '''
    
    cc_dados = ""
    
    ob_lst = []
    
    if isinstance(p_cc_dados, list):
    
        try:
            
            for dado in p_cc_dados:
                if (len(cc_dados) == 0 \
                and len(str(dado.strip())) > 0) \
                or (len(cc_dados) > 0 \
                and len(str(dado.strip())) > 0 \
                and len(cc_dados) > len(str(dado.strip()))) \
                :
                    cc_dados = str(dado.strip())
            
            if len(cc_dados) > 0:
                for dado in p_cc_dados:
                    if len(cc_dados) == len(str(dado.strip())): 
                        ob_lst.append(str(dado.strip()))        
                
                if len(ob_lst) > 1:
                    cc_dados = str(ob_lst[0])
                    for dado in ob_lst:
                        if len(cc_dados) < len(str(dado)):
                            cc_dados = str(dado)        
                            
        except:
        
            pass
    
    return cc_dados.capitalize()

def main():
    """
    Funcao principal
    """
    cc_dado = input("Digita os dados: ")
    
    cc_lista = cc_dado.split(",")
    
    print(fnc_menor_nome(cc_lista))
    
if __name__ == "__main__" :
    """
    Ponto de inicio
    """

    # Aciona a funcao principal
    main()
        
#Fim do programa
