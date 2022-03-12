#coding:utf-8
"""
#Programa, jogo do NIM
"""

def computador_escolhe_jogada (n,m):
    return fnc_computador_escolhe(p_nr_pecas=n, p_nr_limite=m)
    
def fnc_computador_escolhe(p_nr_pecas, p_nr_limite):
    """
    Funcao usuario escolhe
    """
    
    nr_computador_remove = 1

    while nr_computador_remove <= p_nr_limite:
    
        if (p_nr_pecas - nr_computador_remove) % (p_nr_limite+1) == 0:
        
            return nr_computador_remove

        else:
        
            nr_computador_remove += 1

    return nr_computador_remove

def usuario_escolhe_jogada(n,m):
    return fnc_usuario_escolhe(p_nr_limite=m)
    
def fnc_usuario_escolhe(p_nr_limite):
    """
    Funcao usuario escolhe
    """
    
    bl_valido = False

    while not bl_valido:
        try:
        
            nr_jogador_remove = int(input('Quantas peças você vai tirar? '))
   
            if nr_jogador_remove > p_nr_limite \
                or nr_jogador_remove < 1:
        
                print('\nJogada inválida! Tente de novo.\n')
   
            else:
        
                bl_valido = True
        
        except:
            print('\nJogada inválida! Tente de novo.\n')
            
        
    return nr_jogador_remove

def partida():
    fnc_partida()
    
def fnc_partida():
    """
    Funcao partida
    """
    
    bl_valido = False

    while not bl_valido:   
    
        try:
    
            nr_pecas = int(input('Quantas peças? '))

            nr_limite = int(input('Limite de peças por jogada? '))

            bl_valido = True
            
        except:
            pass
        
        
    bl_vez_computador = False

    if nr_pecas % (nr_limite+1) == 0:
    
        print('\nVoce começa!\n')

    else:
    
        print('\nComputador começa!\n')
        
        bl_vez_computador = True

    while nr_pecas > 0:
        
        if bl_vez_computador:
            
            nr_computador_remove = fnc_computador_escolhe(nr_pecas, nr_limite)
            
            nr_pecas -= nr_computador_remove
            
            print('O computador tirou', nr_computador_remove, 'peças')

            bl_vez_computador = False
            
        else:
            
            nr_jogador_remove = fnc_usuario_escolhe(nr_limite)
            
            nr_pecas -= nr_jogador_remove
            
            print('\nVocê tirou', nr_jogador_remove, 'peças.\n')
            
            bl_vez_computador = True
        
        print('Agora restam,', nr_pecas, 'peças no tabuleiro.\n')
                
    print('Fim do jogo! ',end='')
    
    if not bl_vez_computador:
    
        print('Computador Ganhou')

    else:
    
        print('Você Ganhou')
    
    return bl_vez_computador

def campeonato():
    fnc_campeonato()
    
def fnc_campeonato():
    """
    Funcao campeonato
    """
    
    nr_rodada = 1
    
    bl_rodada = False
    
    nr_vitoria_computador = 0
    
    nr_vitoria_jogador = 0
    
    while nr_rodada <= 3:
       
        print('\n**** Rodada', nr_rodada, ' ****\n')
 
        bl_rodada = fnc_partida()
        
        nr_rodada += 1
        
        if bl_rodada:
            
            nr_vitoria_jogador += 1
            
        else:
            
            nr_vitoria_computador += 1
        
        if nr_vitoria_jogador >= 2 \
        or nr_vitoria_computador >= 2:
            break
        
    print('\nPlacar : Você ', nr_vitoria_jogador,' X ' , nr_vitoria_computador,'Computador' )

def inicio():
    main()

def main():
    """
    Funcao principal
    """

    print('\nBem-vindo ao jogo do NIM! \n')
    
    print('1 - para jogar uma partida isolada')
    
    print('2 - para jogar um campeonato [MELHOR DE 3]')

    bl_valido = False

    while not bl_valido:   
    
        try:
    
            print()
    
            nr_escolha = int(input('Escolha: '))
    
            if nr_escolha == 1 or nr_escolha == 2 \
            or nr_escolha == 0:
                bl_valido = True
                
            else:
                print('\nEscolha inválida! Tente de novo.\n')
        
        except:
        
            print('\nEscolha inválida! Tente de novo.\n')
            
    print()
    
    if nr_escolha == 2:
        
        print('\nVoce escolheu um campeonato!\n')
        
        fnc_campeonato()
        
    elif nr_escolha == 1:
        
        print('\nVoce escolheu uma partida!\n')
        
        bl_rodada = fnc_partida()
    
    print('\nFim do jogo\n')

if __name__ == "__main__" :
    """
    Ponto de inicio
    """

    # Aciona a funcao principal
    main()
        
#Fim do programa
