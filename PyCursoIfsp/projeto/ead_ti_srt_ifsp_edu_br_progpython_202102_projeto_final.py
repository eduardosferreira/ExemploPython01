# -*- coding: utf-8 -*-
"""
----------------------------------------------------------------------------------------------
  SISTEMA ..: Curso	SRT0032 - Introdução à programação em Python (Câmpus Sertãozinho)
  MODULO ...: PROJETO FINAL
  SCRIPT ...: ead_ti_srt_ifsp_edu_br_progpython_202102_projeto_final.py
  CRIACAO ..: 11/09/2021
  AUTOR ....: EDUARDO DA SILVA FERREIRA - ST3030521 
  DESCRICAO : 
  - Cria uma estrutura que permita o lançamento de notas para varios aluno
  -- A estrutura será de repetição aonde será com condição de parada
  - Casa aluno terá 3 notas, sendo a nota >= 0 e <= 10. 
  -- Aluno, ira possuir os atributos nome e sexo
  -- Alesm das notas, tambem a media das 3 notas.
  --- Sendo STATUS da media:
  ---- >= 7 : APROVADO
  ---- >= 4 E < 7 : EXAME
  ---- < 4 : REPROVADO

  - Ao final apresente:
  -- TOTAL DE ALUNOS CADASTRADOS
  
  -- QTDE PORCENTUAL DE ALUNOS DE ACORDO COM STATUS:
  --- APROVADOS
  --- EXAME
  --- REPROVADOS

  -- VALORES ABSOLUTOS DE QTDE DE ALUNOS PARA CADA SEXO E PARA CADA STATUS


----------------------------------------------------------------------------------------------
  HISTORICO : 
    * 11/09/2021 - EDUARDO DA SILVA FERREIRA - ST3030521
        - Criacao do script.
----------------------------------------------------------------------------------------------
"""

import datetime

class Aluno:
    """
    Classe Aluno
    """
    # Variavel de codigo (Auto Incremento)
    nr_codigo = int(0)
    nr_intancia = int(0)

    
    def __init__(self, p_nm_nome, p_ds_sexo="", *p_ob_lista_notas):
        """
        ()
        Funcao contrutora da classe
        """
        Aluno.nr_intancia += 1
        Aluno.nr_codigo += 1
        self.__nr_codigo = Aluno.nr_codigo
        self.__nm_nome = str(p_nm_nome).strip()
        if len(self.__nm_nome) == 0:
            raise ValueError("Obrigatório a informação do nome")
        self.__ds_sexo =  "" \
            if len(str(p_ds_sexo).strip()) == 0 else str(p_ds_sexo[0]).strip().upper() \
            if str(p_ds_sexo[0]).strip().upper() in ('M','F') else ""    
        self.__nr_nota_1 = 0
        self.__nr_nota_2 = 0
        self.__nr_nota_3 = 0      
        self.__fnc_atribuir_notas(p_ob_lista_notas)  
       
    def __del__(self):
        '''
            Finaliza os atributos das classes
        '''            
        # Decrementando no fim
        Aluno.nr_intancia -= 1
        self.__del_codigo()


    def __del_codigo(self):
        """
        Apaga o atrito do codigo gerado
        """
        del self.__nr_codigo


    def __fnc_validar_nota(self,p_nr_nota):
        """
        (float) - > float
        Atribui o valor correto da nota
        """
        nr_nota = 0

        try:
            if (p_nr_nota < 0 or p_nr_nota > 10):
                raise ValueError("Intervalo de valores incorreto (0 a 10).")  
            
            nr_nota = p_nr_nota 
                
        except Exception as e:
            raise ValueError("Atribuição incorreto do valor! Por gentileza, verificar ... " + str(p_nr_nota) + " >> " + str(e))
        
        return nr_nota


    def __fnc_atribuir_notas(self,p_ob_lista_notas):
        """
        (lista float)
        Atribui os valores das notas
        """
        if len(p_ob_lista_notas) >= 1:
            self.__nr_nota_1 = self.__fnc_validar_nota(p_ob_lista_notas[0])
        if len(p_ob_lista_notas) >= 2:
            self.__nr_nota_2 = self.__fnc_validar_nota(p_ob_lista_notas[1])
        if len(p_ob_lista_notas) >= 3:
            self.__nr_nota_3 = self.__fnc_validar_nota(p_ob_lista_notas[2])
    
    @property
    def codigo(self):
        return self.__nr_codigo
    
    @property
    def nome(self):
        return str(self.__nm_nome).upper()
    
    @property
    def sexo(self):
        return "Não declarado".upper() \
            if len(str(self.__ds_sexo).strip()) == 0 else "Masculino".upper() \
            if str(self.__ds_sexo[0]).strip().upper() == 'M' else "Feminino".upper()

    @property
    def nota_1(self):
        return self.__nr_nota_1

    @property
    def nota_2(self):
        return self.__nr_nota_2

    @property
    def nota_3(self):
        return self.__nr_nota_3

    @property
    def media(self):
        nr_media = 0
        try:
            nr_media = round((self.nota_1 + \
                       self.nota_2 + \
                       self.nota_3)  
                       / 3,2)       
        except:
            nr_media = 0

        return nr_media

    @property
    def status(self):
        if self.media >= 7:
            return "APROVADO"
        elif self.media < 4:    
            return "REPROVADO"
        else:     
            return "EXAME"

    @nome.setter
    def nome(self, p_nm_nome): 
        raise ValueError("Impossivel alterar diretamente. " + str(p_nm_nome))
    
    @sexo.setter
    def sexo(self, p_ds_sexo): 
        raise ValueError("Impossivel alterar diretamente. " + str(p_ds_sexo))
    
    @nota_1.setter
    def nota_1(self, p_nr_nota): 
        self.__nr_nota_1 = self.__fnc_validar_nota(p_nr_nota)

    @nota_2.setter
    def nota_2(self, p_nr_nota): 
        self.__nr_nota_2 = self.__fnc_validar_nota(p_nr_nota)

    @nota_3.setter
    def nota_3(self, p_nr_nota): 
        self.__nr_nota_3 = self.__fnc_validar_nota(p_nr_nota)

    def __str__(self):
        '''
            Imprimi os dados
        '''
        ds_retorno = " \n << Aluno: " \
                     + " \n - Código: " + str(self.codigo) \
                     + " \n - Nome: " + str(self.nome) \
                     + " \n - Sexo: " + str(self.sexo) \
                     + " \n - Nota do 1 quadrimestre: " + str(self.nota_1) \
                     + " \n - Nota do 2 quadrimestre: " + str(self.nota_2) \
                     + " \n - Nota do 3 quadrimestre: " + str(self.nota_3) \
                     + " \n - Média: " + str(self.media) \
                     + " \n - Status: " + str(self.status) + " \n >> "
        
        return ds_retorno


def dtf():
    """
    () - texto(dd/mm/yyyy hh:mm:ss)
    Retorna data em texto no formato dia mes ano hora minuto segundo
    """
    return (datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

def percent(x, y):
    if not x and not y:
        return "0"
    elif x < 0 or y < 0:
        return "0"
    else:
        final = round(((100 * float(x))/ float(y)),2)
        return str(final)        

def main():
    """
    ()
    Funcao principal a ser acionado
    """
    print("# ",dtf() , " - Início da funcao principal. ")
    
    ob_lista_aluno = []
    p_nr_retorno = 0
    while not p_nr_retorno:
        cc_dados_aluno = str(input('''
        Informe os dados do aluno, separados por ';' : 
        - (Obrigatório) Nome
        - Sexo (M ou F)
        - Notas do 1 quadrimestre (0 a 10 ; casa decimal separado por "." ; Ex. 8.9 E igual 8,9)
        - Notas do 2 quadrimestre (0 a 10 ; casa decimal separado por "." ; Ex. 8.9 E igual 8,9)
        - Notas do 3 quadrimestre (0 a 10 ; casa decimal separado por "." ; Ex. 8.9 E igual 8,9)
        Exemplo : Eduardo ; M ; 10 ; 8.9 ; 9
        (P/ sair clica em <<Enter>>) 
        - > : ''')).strip()
        p_nr_retorno = 1 if len(cc_dados_aluno) == 0 else 0    
        if not p_nr_retorno:
            try:
                ob_dados_aluno = cc_dados_aluno.split(";")
                if len(ob_dados_aluno) == 0:
                    raise ValueError("-Nenhuma informação digitada ... ")
                else:
                    if len(str(ob_dados_aluno[0]).strip()) == 0:
                        raise ValueError("-Nome do aluno obrigatório ... ")
                    else:
                        nm_nome = str(ob_dados_aluno[0]).strip()
                        ds_sexo = ""
                        nr_nota_1 = 0
                        nr_nota_2 = 0
                        nr_nota_3 = 0                        
                        if len(ob_dados_aluno) >= 2:
                            ds_sexo = str(ob_dados_aluno[1]).strip().upper()
                        if len(ob_dados_aluno) >= 3:
                            nr_nota_1 = float(str(ob_dados_aluno[2]).strip())
                        if len(ob_dados_aluno) >= 4:
                            nr_nota_2 = float(str(ob_dados_aluno[3]).strip())
                        if len(ob_dados_aluno) >= 5:
                            nr_nota_3 = float(str(ob_dados_aluno[4]).strip())
                        ob_aluno = Aluno(nm_nome,ds_sexo,nr_nota_1,nr_nota_2,nr_nota_3)
                        print(ob_aluno)
                        confirma = str(input("Confirme os dados [S/N] ? ")).strip().upper()
                        if len(confirma) > 0:
                            if str(confirma[0]) == "S":
                                ob_lista_aluno.append(ob_aluno)
            except Exception as e:
                print("\nFALHA nas informações do aluno!","\n",str(e)) 

        print("\n")


    if len(ob_lista_aluno) > 0:
        print("# ",dtf() , "*"*100)
        print("# ",dtf() , "Lista de Alunos")

        v_nr_tot = len(ob_lista_aluno)
        v_qt_aprovado = 0
        v_qt_m_aprovado = 0
        v_qt_f_aprovado = 0
        v_qt_s_aprovado = 0
        v_qt_reprovado = 0
        v_qt_m_reprovado = 0
        v_qt_f_reprovado = 0
        v_qt_s_reprovado = 0
        v_qt_exame = 0
        v_qt_m_exame = 0
        v_qt_f_exame = 0
        v_qt_s_exame = 0
        
        for aluno in ob_lista_aluno:
            print(aluno)
            if str(aluno.status).strip().upper() == "APROVADO":
                v_qt_aprovado += 1
                if str(aluno.sexo).upper().strip().startswith("M"):
                    v_qt_m_aprovado += 1
                elif str(aluno.sexo).upper().strip().startswith("F"):
                    v_qt_f_aprovado += 1
                else:         
                    v_qt_s_aprovado += 1        
            if str(aluno.status).strip().upper() == "REPROVADO":
                v_qt_reprovado += 1
                if str(aluno.sexo).upper().strip().startswith("M"):
                    v_qt_m_reprovado += 1
                elif str(aluno.sexo).upper().strip().startswith("F"):
                    v_qt_f_reprovado += 1
                else:         
                    v_qt_s_reprovado += 1        
            if str(aluno.status).strip().upper() == "EXAME":
                v_qt_exame += 1
                if str(aluno.sexo).upper().strip().startswith("M"):
                    v_qt_m_exame += 1
                elif str(aluno.sexo).upper().strip().startswith("F"):
                    v_qt_f_exame += 1
                else:         
                    v_qt_s_exame += 1

        print("# ",dtf() , "*"*100)

        print("# ",dtf() , "*"*100)
        print("# ",dtf() , "Relatório de Alunos")

        print("# ",dtf() , "Quantidade TOTAL de ALUNOS: ",str(v_nr_tot))
        print("# ",dtf() , "PORCENTAGEL de ALUNOS -> STATUS APROVADO: ",percent(v_qt_aprovado,v_nr_tot))
        print("# ",dtf() , "Quantidade TOTAL de ALUNOS -> STATUS APROVADO: ",str(v_qt_aprovado))        
        print("# ",dtf() , "Quantidade TOTAL de ALUNOS -> SEXO : MASCULINO -> STATUS APROVADO: ",str(v_qt_m_aprovado))
        print("# ",dtf() , "Quantidade TOTAL de ALUNOS -> SEXO : FEMININO -> STATUS APROVADO: ",str(v_qt_f_aprovado))
        print("# ",dtf() , "Quantidade TOTAL de ALUNOS -> SEXO : NAO DECLARADO -> STATUS APROVADO: ",str(v_qt_s_aprovado))
        print("# ",dtf() , "PORCENTAGEL de ALUNOS -> STATUS REPROVADO: ",percent(v_qt_reprovado,v_nr_tot))
        print("# ",dtf() , "Quantidade TOTAL de ALUNOS -> STATUS REPROVADO: ",str(v_qt_reprovado))
        print("# ",dtf() , "Quantidade TOTAL de ALUNOS -> SEXO : MASCULINO -> STATUS REPROVADO: ",str(v_qt_m_reprovado))
        print("# ",dtf() , "Quantidade TOTAL de ALUNOS -> SEXO : FEMININO -> STATUS REPROVADO: ",str(v_qt_f_reprovado))
        print("# ",dtf() , "Quantidade TOTAL de ALUNOS -> SEXO : NAO DECLARADO -> STATUS REPROVADO: ",str(v_qt_s_reprovado))
        print("# ",dtf() , "PORCENTAGEL de ALUNOS -> STATUS EXAME: ",percent(v_qt_exame,v_nr_tot))
        print("# ",dtf() , "Quantidade TOTAL de ALUNOS -> STATUS EXAME: ",str(v_qt_exame))
        print("# ",dtf() , "Quantidade TOTAL de ALUNOS -> SEXO : MASCULINO -> STATUS EXAME: ",str(v_qt_m_exame))
        print("# ",dtf() , "Quantidade TOTAL de ALUNOS -> SEXO : FEMININO -> STATUS EXAME: ",str(v_qt_f_exame))
        print("# ",dtf() , "Quantidade TOTAL de ALUNOS -> SEXO : NAO DECLARADO -> STATUS EXAME: ",str(v_qt_s_exame))
        

        print("# ",dtf() , "*"*100)
        
    else:
        print("# ",dtf() , "*"*100)
        print("# ",dtf() , "NÃO FOI CADASTRADOS NENHUM ALUNO!")
        print("# ",dtf() , "*"*100)
        

    print("\n","\n","\n")    
    print("# ",dtf() , " - Fim do da funcao principal. ")


if __name__ == "__main__":
    """
    Ponto inicial de start
    """
    print("# ",dtf() , " - Início do processamento. ")
    main()   
    print("# ",dtf() , " - Fim do processamento. ")

 