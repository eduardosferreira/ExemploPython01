#coding:utf-8
"""
#Programa 
    Bhaskara   
"""

# importa os objetos
import math

# Inicio da Classes
class Bhaskara:
    '''
        Classe que calcula formula baskara 
    '''    
    def __init__(self, **kwargs):
        '''
            (float, float, float) -> Metodo construtor
            Inicializa os atributos das classes
        '''        
        # variaveis principais
        self.__nr_a = float(0)
        self.__nr_b = float(0)
        self.__nr_c = float(0)
        
        # variaveis auxiliares
        self.__nr_delta = float(0)
        self.__qt_raizes = -1
        self.__nr_raiz_1 = float(0)
        self.__nr_raiz_2 = float(0)
        
        # *kargs for variable number of keyword arguments
        for key, value in kwargs.items():
            if str(key).upper().strip() == "NR_A":
                try:
                    self.__nr_a = float(value)
                except:
                    self.__nr_a = float(0)   
            elif str(key).upper().strip() == "NR_B":
                try:
                    self.__nr_b = float(value)
                except:
                    self.__nr_b = float(0)   
            elif str(key).upper().strip() == "NR_C":
                try:
                    self.__nr_c = float(value)
                except:
                    self.__nr_c = float(0)   
        
        self.__nr_retorno = int(0)    
    
    
    # function to delete attribute
    def del_nr_retorno(self):
         del self.__nr_retorno
    
    # using property decorator
    # a getter function
    @property
    def nr_retorno(self): 
        return self.__nr_retorno

    
    @property
    def nr_delta(self): 
        return self.__nr_delta


    @property
    def nr_raiz_1(self): 
        return self.__nr_raiz_1


    @property
    def nr_raiz_2(self): 
        return self.__nr_raiz_2

    @property
    def qt_raizes(self): 
        return self.__qt_raizes


    @property
    def nr_a(self): 
        return self.__nr_a


    @property
    def nr_b(self): 
        return self.__nr_a

    
    @property
    def nr_c(self): 
        return self.__nr_c
        
    # set
    # a setter function    
    @nr_retorno.setter
    def nr_retorno(self, p_nr_aux): 
        self.__nr_retorno = p_nr_aux


    @nr_delta.setter
    def nr_delta(self, p_nr_aux): 
        raise ValueError("Impossivel alterar diretamente. " + str(p_nr_aux))

        
    @nr_a.setter
    def nr_a(self, p_nr_aux): 
        if self.__qt_raizes == -1:
            try:
                nr_aux = float(p_nr_aux)
                self.__nr_a = nr_aux
            except:
                raise ValueError("Impossivel alterar o valor! " + str(p_nr_aux))
        else:
            raise ValueError("Impossivel alterar o valor! " + str(p_nr_aux))    

    
    @nr_b.setter
    def nr_b(self, p_nr_aux): 
        if self.__qt_raizes == -1:
            try:
                nr_aux = float(p_nr_aux)
                self.__nr_b = nr_aux
            except:
                raise ValueError("Impossivel alterar o valor! " + str(p_nr_aux))
        else:
            raise ValueError("Impossivel alterar o valor! " + str(p_nr_aux))    


    @nr_c.setter
    def nr_c(self, p_nr_aux): 
        if self.__qt_raizes == -1:
            try:
                nr_aux = float(p_nr_aux)
                self.__nr_c = nr_aux
            except:
                raise ValueError("Impossivel alterar o valor! " + str(p_nr_aux))
        else:
            raise ValueError("Impossivel alterar o valor! " + str(p_nr_aux))    


    def fnc_carregar_dados(self, *argv):
        '''
            Entrada com input de dados
        '''
        nr_retorno = int(0)
        
        nr_contador = int(0)
        for arg in argv:
            nr_contador += 1
            if nr_contador == 1:
                try:
                    self.__nr_a = float(arg)
                except:
                    self.__nr_a = float(0)   
            elif nr_contador == 2:
                try:
                    self.__nr_b = float(arg)
                except:
                    self.__nr_b = float(0)   
            elif nr_contador == 3:
                try:
                    self.__nr_c = float(arg)
                except:
                    self.__nr_c = float(0)   
            
        if self.__nr_a > 0 \
        and self.__nr_b > 0 \
        and self.__nr_c > 0:
            return nr_retorno
        
        print("*"*100)
        print()
        
        print(str("Entra com dados para calculo de Bhaskara").center(100))
        
        print()
        
        if self.__nr_a <= 0:
            try:
                self.__nr_a = float(input("Informe a entrada de A (decimal): "))
            except:
                print("Entrada inválida!")
                self.__nr_a = 0
                nr_retorno += 1
        
        if not nr_retorno:
            if self.__nr_b <= 0:
                try:
                    self.__nr_b = float(input("Informe a entrada de B (decimal): "))
                except:
                    print("Entrada inválida!")
                    self.__nr_b = 0
                    nr_retorno += 1
        
        if not nr_retorno:
            if self.__nr_c <= 0:
                try:
                    self.__nr_c = float(input("Informe a entrada de C (decimal): "))
                except:
                    print("Entrada inválida!")
                    self.__nr_c = 0
                    nr_retorno += 1
            
        print()
        print("*"*100)
        return nr_retorno

    
    def __str__(self):
        '''
            Imprimi os dados
        '''
        ds_retorno = ""
        ds_retorno += "\n" + "*"*100 + "\n"
        
        ds_retorno += str("Retorno calculo de Bhaskara").center(100)
        
        ds_retorno += "\n"
        
        ds_retorno += "\nA:" + str(self.__nr_a)
        
        ds_retorno += "\nB:" + str(self.__nr_b)
        
        ds_retorno += "\nC:" + str(self.__nr_c)
        
        ds_retorno += "\n"
        
        if self.__qt_raizes <= 0:
            ds_retorno += "\n Não tem raizes\n"
            
        if self.__qt_raizes >= 1:
            ds_retorno += "\n Raiz 1 : " + str(self.__nr_raiz_1) 
        
        if self.__qt_raizes > 1:
            ds_retorno += "\n Raiz 2 : " + str(self.__nr_raiz_2)
            
        ds_retorno += "\n" + "*"*100 + "\n"
        
        return ds_retorno
    
    
    def fnc_calcula_delta (self):
        '''
            () -> float
            Retorna calculo da variante delta
        '''        
        return self.__nr_b**2 - 4 * self.__nr_a * self.__nr_c
        
    
    def fnc_calcula_raiz(self,p_nr_raiz=1):
        '''
            (float) -> float
            Retorna calculo da variante raiz 
        '''        
        if self.__nr_a == 0:
            return 0
    
        if p_nr_raiz == 1:
            return ((-self.__nr_b) + math.sqrt(self.__nr_delta))/(2*self.__nr_a)  
        else:
            return ((-self.__nr_b) - math.sqrt(self.__nr_delta))/(2*self.__nr_a)  
    
    
    def fnc_calcula_raizes(self):
        '''
            () -> int, float, float
            Retorna calculo das raiz, sendo os retornos: 
            primeiro : quantidade de raizes retornadas
            segundo  : primeira raiz 
            terceiro : segunda  raiz 
        '''        
        # declaracao de variaveis
        self.__nr_delta = float(0)
        self.__qt_raizes = int(0)
        self.__nr_raiz_1 = float(0)
        self.__nr_raiz_2 = float(0)
        
        # calcula delta
        nr_delta = self.fnc_calcula_delta ()
        
        if nr_delta >= 0:
            self.__nr_raiz_1 = self.fnc_calcula_raiz()
            self.__qt_raizes += 1
            
        if nr_delta > 0:
            self.__nr_raiz_2 = self.fnc_calcula_raiz(2)
            self.__qt_raizes += 1
            
        return self.__qt_raizes, self.__nr_raiz_1, self.__nr_raiz_2


# Fim da Classes

#Inicio do programa
def main():
    '''
        Funcao principal do programa
    '''
  
    ob_bhaskara = Bhaskara()
    ob_bhaskara.retorno = ob_bhaskara.fnc_carregar_dados()
    if ob_bhaskara.retorno > 0:
        print("\n***FALHA***\n")
    else:
        print("\n***CALCULO BHASKARA***\n")
        ob_bhaskara.tuple_retorno = \
        tuple(ob_bhaskara.fnc_calcula_raizes())
        print(ob_bhaskara)
        print()
        print(str(ob_bhaskara.tuple_retorno))
        
        
if __name__ == "__main__" :
    """
        Ponto de inicio caso seja acionado diretamente (sem import) 
    """
    # Aciona a funcao principal
    main()
        
#Fim do programa
        