#coding:utf-8
"""
#Programa 
    Triangulo   
"""

# Inicio da Classes
class Triangulo:
   
    # Variavel de contador
    gv_nr_contador = int(0)
        
        
    # function to delete attribute
    def __del_nr_perimetro(self):
         del self.__nr_perimetro
    
    # using property decorator
    # a getter function
    @property
    def a(self): 
        return self.__a

    
    @property
    def b(self): 
        return self.__b


    @property
    def c(self): 
        return self.__c

        
    # set
    # a setter function    
    @a.setter
    def a(self, p_nr_aux): 
        try:
            nr_aux = int(p_nr_aux)
            self.__a = nr_aux
        except:
            raise ValueError("Impossivel alterar o valor! " + str(p_nr_aux))

        
    @b.setter
    def b(self, p_nr_aux): 
        try:
            nr_aux = int(p_nr_aux)
            self.__b = nr_aux
        except:
            raise ValueError("Impossivel alterar o valor! " + str(p_nr_aux))


    @c.setter
    def c(self, p_nr_aux): 
        try:
            nr_aux = int(p_nr_aux)
            self.__c = nr_aux
        except:
            raise ValueError("Impossivel alterar o valor! " + str(p_nr_aux))

            
    def fnc_carregar_dados(self, p_fl_carrega=0, *argv):
        '''
            Entrada com input de dados
        '''
        nr_retorno = int(0)
        
        nr_retorno = int(0)
        for arg in argv:
            nr_retorno += 1
            if nr_retorno == 1:
                try:
                    self.a = arg
                except:
                    pass
                    
            elif nr_retorno == 2:
                try:
                    self.b = arg
                except:
                    pass
                    
            elif nr_retorno == 3:
                try:
                    self.c = arg
                except:
                    pass
            
        if (self.a > 0 \
        and self.b > 0 \
        and self.c > 0) \
        or p_fl_carrega != 0:
            return nr_retorno
        
        
        print("*"*100)
        print()
        
        print(str("Entra com dados ").center(100))
        
        print()
        
        if self.a <= 0:
            try:
                self.a = int(input("Informe a entrada de A (inteiro): "))
            except:
                print("Entrada inválida!")
                nr_retorno += 1
        
        if not nr_retorno:
            if self.b <= 0:
                try:
                    self.b = int(input("Informe a entrada de B (inteiro): "))
                except:
                    print("Entrada inválida!")
                    nr_retorno += 1
        
        if not nr_retorno:
            if self.c <= 0:
                try:
                    self.c = int(input("Informe a entrada de C (inteiro): "))
                except:
                    print("Entrada inválida!")
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
        
        ds_retorno += str(" TRIANGULO ( " + str(Triangulo.gv_nr_contador) + " )").center(100)
        
        ds_retorno += "\n"
        
        ds_retorno += "\nA: " + str(self.a)
        
        ds_retorno += "\nB: " + str(self.b)
        
        ds_retorno += "\nC: " + str(self.c)
        
        ds_retorno += "\n"        
        
        ds_retorno += str(" \n PERIMETRO = " + str(self.perimetro()) + " \n ").center(30)
        
        ds_retorno += str(" \n TIPO = " + str(self.tipo_lado()).upper() + " \n ").center(30)
                
        ds_retorno += "\n" + "*"*100 + "\n"
        
        return ds_retorno


    def __init__(self, p_nr_lado_a=0, p_nr_lado_b=0, p_nr_lado_c=0):
        '''
            (int, int, int) -> Metodo construtor
            Inicializa os atributos das classes
        '''        
        # variaveis principais
        self.__a = int(0)
        self.__b = int(0)
        self.__c = int(0)
        
        # variaveis auxiliares
        self.__nr_perimetro = int(0)
        self.__tp_lado = ""    
    
        nr_aux = self.fnc_carregar_dados(1,p_nr_lado_a, p_nr_lado_b, p_nr_lado_c)
        
        self.__fnc_calcula_perimetro()
        
        Triangulo.gv_nr_contador += 1


    def __del__(self):
        '''
            Finaliza os atributos das classes
        '''            
        # Decrementando no fim
        Triangulo.gv_nr_contador -= 1
        self.__del_nr_perimetro()

    def __fnc_calcula_perimetro(self): 
        '''
            Calcula o perimetro
        '''              
        self.__nr_perimetro = self.a + self.b + self.c     
    
    
    def perimetro(self):
        self.__fnc_calcula_perimetro()
        return self.__nr_perimetro

    
    def __fnc_calcula_tipo_lado(self): 
        '''
            Calcula o perimetro
        '''              
        if (self.a == self.b)  \
        and (self.b == self.c):
            self.__tp_lado = "equilátero"
        
        elif (self.a != self.b)  \
        and (self.b != self.c) \
        and (self.a != self.c) \
        :
            self.__tp_lado = "escaleno"
        
        elif (self.a == self.b)  \
        or (self.b == self.c) \
        or (self.a == self.c) \
        :     
            self.__tp_lado = "isósceles"
    
    def tipo_lado(self):
        self.__fnc_calcula_tipo_lado()
        return self.__tp_lado
    
# Fim da Classes

#Inicio do programa
def main():
    '''
        Funcao principal do programa
    '''
  
    ob_a = Triangulo()    
    
    nr_retorno = ob_a.fnc_carregar_dados()    
   
    print(str(ob_a))    
   
    
if __name__ == "__main__" :
    """
        Ponto de inicio caso seja acionado diretamente (sem import) 
    """
    # Aciona a funcao principal
    main()
        
#Fim do programa
        