#coding:utf-8
"""
#Programa 
       
"""
#Inicio do programa

def fnc_busca_sequencial(p_ob_lista_sequencia=None, p_nr_procura=None,p_fl_mensagem=False):
    '''
        (list, float) -> bool
        Funcao busca de sequencial
    ''' 
    fl_retorno = True
    
    if p_ob_lista_sequencia is None:
        p_ob_lista_sequencia = fnc_cria_array()
    else:
        if not isinstance(p_ob_lista_sequencia, list):
            fl_retorno = False
    
    if fl_retorno:
        if len(p_ob_lista_sequencia) == 0:
            fl_retorno = False
    
    if fl_retorno:
        bl_valida_entrada = False
        if p_nr_procura is None:
            bl_valida_entrada = True
        else:
            if not (isinstance(p_nr_procura, float) \
            or isinstance(p_nr_procura, int)):
                fl_retorno = False
    
    if fl_retorno:
        # numero
        while bl_valida_entrada:
            try:
                p_nr_procura = float(input("Entra com numero : "))
                bl_valida_entrada = False
            except:
                print("Entrada incorreto!")
        
    if fl_retorno:
        fl_retorno = False
        for nr_index in range(len(p_ob_lista_sequencia)):
            if isinstance(p_ob_lista_sequencia[nr_index], float) \
            or isinstance(p_ob_lista_sequencia[nr_index], int):
                if p_ob_lista_sequencia[nr_index] == p_nr_procura:
                    fl_retorno = True
                    break
    
    if p_fl_mensagem:
        if fl_retorno:
            print("Encontrou !!!",str(p_ob_lista_sequencia)," -> ",str(p_nr_procura))
        else:
            print("Não Encontrou !!!",str(p_ob_lista_sequencia)," -> ",str(p_nr_procura))
        
    return fl_retorno    

    
def fnc_cria_array():
    '''
        Funcao cria array
    '''
    # criacao variaveis
    ob_lst = []
    nr_qtde_elementos = 0
    nr_elemento = 0
    bl_valida_entrada = True
    
    # numero de elementos
    while bl_valida_entrada:
        try:
            nr_qtde_elementos = int(input("Entra com numero de elementos : "))
            bl_valida_entrada = False
        except:
            print("Entrada incorreto!")
            
    if nr_qtde_elementos <= 0:
        print("Entrada menor que o permitido! FIM ...")
        return ob_lst
         
    # interacao
    for nr_idx in range(0, nr_qtde_elementos):
        bl_valida_entrada = True
        while bl_valida_entrada:
            try:
                nr_elemento = int(input("Elemento: "))
                ob_lst.append(nr_elemento) # adicao de elementos
                bl_valida_entrada = False
            except:
                print("Entrada incorreto!")            
    
    print("Lista ...")
        
    print(str(ob_lst))
    
    return ob_lst
    
def main():
    '''
        Funcao principal do programa
    '''
    fl_retorno = fnc_busca_sequencial(p_fl_mensagem=True)
    
    fl_retorno = fnc_busca_sequencial([1,2,3,4.2],1.2,True)    

if __name__ == "__main__" :
    """
        Ponto de inicio caso seja acionado diretamente (sem import) 
    """
    # Aciona a funcao principal
    main()
        
#Fim do programa