"""
Curso.....: Python Fundamentos para Análise de Dados
>> https://www.datascienceacademy.com.br/
Aluno.....: Eduardo da Silva Ferreira
Capítulo..: 2 - Variaveis, Tipos e Estruturas
"""

# Dicas
# Indentação  : Essencial para python, tab ou espacos, mas nunca os dois
# Comentários : # cerquilha ou """ ... """ 3 espaços duplos
from typing import List, Union, Tuple

"""
Conselhos:
- Clareza é importante, mantenha codigo limpo e organizado;
- ** Código esparso (com espaco entre as linhas) é melhor que denso;sd
- Documente sempre o codigo, não existe limite
- Siga os padroes (PEP) não para criar complexidade, mas para manter a regra
- Errros nunca serão silenciosos, a menos que propositalmente
- ** Simples é melhor que complexo, complexo é melhor que complicado
- Não se sinta obrigado a criar classes, sem uma boa razão
"""

"""
Tipos:
https://docs.python.org/3.11/
int   >> inteiros -> Ex: 3
float >> pontos flutuantes ->  Ex: 3.2121
+ soma, - dubstração, * Multiplicação, / Divisão, // Divisao de numero inteiro
% mdoulo , ** potencia
int() converte para inteiro --> int (3.2)
float() convert para float -- > 2.0

Operadores
== igualdade, != Desigualdade, > maior, < menor
>= maior ou igual, <= menor ou igual

Diversos
Guia de desenvolvimento : https://devguide.python.org/

Operadores de Atribuição
  = atribuicao Ex. z   = 10
 += soma       Ex. z  += 10 (equivalente z = z + 10)
 mesmo ocorre para demais -=, *=, /=, %=, **=, //=
Anotação :
Em python, a indexação começa por zero
"""

"""
atribuicao simples
z = 10
z += 10
print(z)
print(4+2)
print(int(6.1))
"""

"""
atribuicao multiplo
a, b, c = 5, 6, 7
print(a)
print(b)
print(c)
"""

"""
p1, p2, p3 = "Maria", 'Eduardo', "jose'
print(p1);
print(p2);
print(p3);
"""
"""
p3 = p2 = p1 = '"Maria", "Eduardo", "jose"'
p1 += "teste"
print(p1)
print(p2)
print(p3)
"""

"""
# Em python, a indexação começa por zero
texto = "Python"
print(texto[0])
print(texto[1])
print(str(len(texto)) + " texto ")
"""

# print("Quebra \n de \n Linha ")

"""

    # Podemos usar um : para executar um slicing que faz a leitura de tudo até
    # um ponto designado. Por exemplo:
    string = "0123456789"
    # print(string[1:])      # Resultado : 123456789 , busca a partir posicao
    # do indice 1 (2 caracter)
    # lembrando que inicializa com zero
    # print(string[:1])      # Resultado : 0, busca até a posicao do indice
    # print(string[:-1])     # Resultado : 012345678, busca todos,
    # exceto ultimo
    # print(string[-1:])     # Resultado : 9, busca ultimo
    # print(string[:])       # Resultado : 0123456789, busca todos
    # print(string[2:6])     # Resultado : 2345, busca indice 2 (3 letra)
    # até indice 6 (7 letra)
    # Resultado : 02468, busca fatiado, em 2 em 2 caracter
    # print(string[::2])
    # Resultado : 9876543210, busca os registros ao contrario
    # print(string[::-1])
    # Resultado : 864, busca ao contrario, sendo o inicio, é o contrario,
    # quebrando em 2 caracteres
    # print(string[8:3:-2])
    # Resultado : 246, busca quebrado, a partir do indice
    # print(string[2:8:2])

"""

"""
    variavel = "eduardo da silva ferreira"
    letras = variavel[0]*3
    # Podemos usar o símbolo de multiplicação para criar repetição!
    letra = 'w'
    letra *= 3

    # string e umutavel, não pode susbtituir
    # letras[0] = "a"  # isto ira gerar erro, não pode realizar

    print(variavel)

    print("\n" + "*" * 100)

    print(letras)

    print("\n" + "*" * 100)

    print(letra)

    print("\n" + "*" * 100)

    # print(variavel.upper())
    # print(variavel.lower())
    # print(variavel.capitalize())  # Primeira letra maisucla
    # print(variavel.split())  # quebra, o espaco por default, e o fator
    # de quebra
    # quebra, o espaco por default, e o fator de quebra
    # print(variavel.split()[0].capitalize())
    # print(variavel.split()[0].split("d"))  # quebra por alguma letra que
    # deseja

    print(variavel.count("e", 10))
"""

"""
    string = "Python is incrivel"

    print(string + " >> Centered String: ", string.center(30, '*'))

    print(string + " >> Left String: ", string.ljust(30, '*'))

    print(string + " >> Rigth String: ", string.rjust(30, '*'))

    print("\n" + "*" * 100)

    name = "M234onica"
    print(name.isalnum())

    # contains whitespace
    name = "M3onica Gell22er "  # -- False , contem espaço
    print(name.isalnum())

    name = "Mo3nicaGell22er"
    print(name.isalnum())

    name = "133"
    print(name.isalnum())

    name = "abcdefgh"
    print(name.isalnum())

    if name.isalnum():
        print("All characters of string (name) are alphanumeric.")
    else:
        print("All characters are not alphanumeric.")

    name = "Monica"  # -- True
    print(name.isalpha())

    # contains whitespace -- False
    name = "Monica Geller"
    print(name.isalpha())

    # contains whitespace -- True
    name = "Monica Geller"
    print(name.replace(" ", "").isalpha())

    # contains number -- Falase
    name = "Mo3nicaGell22er"
    print(name.isalpha())

    print("Python" == "Python")  # True
    print("Python" == "python")  # False
    if True == True:
        print("True")

Lista:


"""

"""
desativar autocorreção, desativa Pylance

Desabilita isso ai .... Format On Save
"[python]": {
        "editor.formatOnSave": false
    },
  
    "editor.codeActionsOnSave": {
        "source.fixAll": false,
        "source.organizeImports": false
      },
      "editor.formatOnSave": false

"""

"""
    lista1 = ["1,2,3,4,5,6,7"]
    lista2 = [1, 2, '3', '4', "5", "6", "7"]
    print(lista1[0])
    print(lista2[0])
    print(lista1, lista2)
    del lista1[0]
    del lista2[0]
    print(lista1, lista2)
    lista2[0] = lista2[1]
    print(lista1, lista2)
    del lista2
"""


def lista1():
    """
    l_old = [1, 'Aspas simples', "Aspas Duplas", 2.3, "string", "string"]
    l_new = []

    for item in l_old:
        l_new.append (item)

    print (str (l_new) + ' >> ' + str (l_old))

    A = ["a", "b", "c"]
    StrA = "".join (A)
    print (StrA)
    ListA = str ( )
    ## StrA is "abc"


    # Dica : https://www.delftstack.com/pt/howto/python/how-to-convert-a-list-to-string/
    a = [1, 2, 3]
    a1 = "".join ([str (_) for _ in a])
    print (a1)

    a = [1, 2, 3]
    a1 = "".join (map (str, a))
    print (a1)

    list1 = ['primeiro', 'segundo', 'terceiro']
    a = ', '.join (list1)
    print (a)

    a = "String"
    l2 = list(a)
    print (l2)

    """
    s = "a"
    n = 1
    a1 = [1, 2, 3]
    list1 = ['primeiro', 'segundo', 'terceiro']
    list1.extend (a1)  # Add uma lista
    list1.append (a1)  # Adiciona um elemento
    print (list1)


"""
https://diegomariano.com/como-ordenar-um-dicionario-em-python/
Dicionários em Python são um tipo de dado que armazena chaves e valores. Entretanto, caso seja necessário ordenar seus dados, eles serão posicionados de acordo com a chave:

d = {'cachorro':2, 'gato':3, 'elefante':1 }

print(sorted(d))  # ['cachorro', 'elefante', 'gato']
Observe que os valores foram ordenados de acordo com a primeira letra de cada chave e não de acordo com os valores de cada chave.

Veja ainda que utilizamos a função sorted(). Note que dicionários não possuem o método sort().

print(d.sort()) 

# AttributeError: 'dict' object has no attribute 'sort' 
Então como ordenar um dicionário de acordo com os valores?

Ordenando dicionários pelos valores
Em certas situações pode ser necessário exibir os dados de um dicionário Python ordenado pelos valores. Podemos fazer isso da seguinte forma:

d = {'cachorro':2, 'gato':3, 'elefante':1 }

for i in sorted(d, key = d.get):
    print(i, d[i])

# elefante 1
# cachorro 2
# gato 3
Ordenação decrescente
Para ordenar do maior para o menor, utilize o parâmetro reverse=True:

d = {'cachorro':2, 'gato':3, 'elefante':1 }

for i in sorted(d, key = d.get, reverse=True):
    print(i, d[i])

# gato 3
# cachorro 2
# elefante 1

https://qastack.com.br/programming/9001509/how-can-i-sort-a-dictionary-by-key

In [1]: import collections

In [2]: d = {2:3, 1:89, 4:5, 3:0}

In [3]: od = collections.OrderedDict(sorted(d.items()))

In [4]: od
Out[4]: OrderedDict([(1, 89), (2, 3), (3, 0), (4, 5)])


"""

"""
def lista2():
    None
    lst1 = []
    a = ['Eduardo',1,"2"]
    b = "a"
    lst1.append(a) # adicionar a salacoa
    lst1.extend(a) # pegar elementos da sacola e adicionar
    print(lst1[0][-1:])
"""

exfuncaolambada = lambda x, y: x * y
exfuncaolambada2 = lambda: 5 * 5

"""
def ex1(*argumentos):
    print (str(argumentos))
    lst = list(argumentos).copy()
    print (str(lst))
    print(exfuncaolambada(5,2))
    print (exfuncaolambada2())
"""

"""
    # Import math library
    import math

    # Round a number upward to its nearest integer
    print (math.ceil (1.4))
    print (math.ceil (5.3))
    print (math.ceil (-5.3))
    print (math.ceil (22.6))
    print (math.ceil (10.0))
"""


def tuplaEx1():
    """
    tupla1 = 1,2,3,4,"a",'b','c',[10,12,13]
    print(tupla1)
    tupla2 = (1,2,3,4,"a",'b','c',[10,12,13])
    print(tupla1)
    naotupla1 = ("ex")
    print (type(naotupla1))
    ehtupla1 = ("ex",)
    print (type(ehtupla1))
    """
    my_tupla1: Tuple[str, int, int, int] = ('a', 1, 2, 4)
    my_lista1 = ['a', "b", "x", 1, 2, 4]
    my_tupla2 = ("0", "1", my_lista1, "3x", 'x1', 'x2', 11, 12, 13)

    # my_lista1[0] = 'b'
    # print (my_lista1[0])
    # print (my_tupla1[0])
    # my_tupla1[0] = 'b' # nao aceita modifica elemento
    # print (my_tupla2)
    # my_tupla2[2][1] = 'b' # posso alterar item tupla, caso seja uma lista o item
    # print (my_tupla1)
    # print (my_tupla2)
    # print (len(my_tupla1))
    # print (len(my_lista1))

    # print(my_lista1.index('x'))
    # print(my_lista1.index(1))

    print (my_tupla2.index ('x1'))
    print (my_tupla2.index (11))


"""
Dicionario
"""


def dicEx1():
    dict_cfop = {'cfop': {'tipo': []}}
    prot_s = {}
    prot_s['protocolado'] = [1, 2, 3, 4]
    dict_cfop['cfop'].update (prot_s)
    reg_s = {}
    reg_s['regerado'] = [11, 12, 13, 14]
    dict_cfop['cfop'].update (reg_s)
    # dict_cfop['cfop'].keys ( )
    # dict_cfop['cfop'].keys ( )
    # dict_cfop.keys ( )
    # dict_cfop['cfop'].values ( )
    # dict_cfop['cfop'].values ( )
    # dict_cfop.values ( )
    # dict_cfop['cfop'].itens ( )
    # dict_cfop['cfop'].items ( )
    # dict_cfop['cfop'].items ( )
    for k, v in dict_cfop['cfop'].items ( ):
        print ('k: ' + str (k) + ' >> v: ' + str (v))
    for k, v in dict_cfop.items ( ):
        print ('k: ' + str (k) + ' >> v: ' + str (v))
    for k, v in dict_cfop['cfop'].items ( ):
        print ('k: ' + str (k) + '')
        for v1 in v:
            print (' >> v1: ' + str (v1))


# https://panda.ime.usp.br/pensepy/static/pensepy/11-Dicionarios/dicionarios.html
"""
keys

nenhum

Retorna uma vista das chaves no dicionário

values

nenhum

Retorna uma vista dos valores no dicionário

items

nenhum

Retorna uma vista dos pares chave-valor no dicionário

get

key

Retorna o valor associado com a chave; ou None

get

key,alt

Retorna o valor associado com a chave; ou alt

mydict = {"cat":12, "dog":6, "elephant":23}
mydict["mouse"] = mydict["cat"] + mydict["dog"]
mydict
print(mydict["mouse"])
18
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
for akey in inventory.keys():     # the order in which we get the keys is not defined
   print("Got key", akey, "which maps to value", inventory[akey])
​
ks = list(inventory.keys())
print(ks)
​
for k in inventory:
   print("Got key", k)
Got key apples which maps to value 430
Got key bananas which maps to value 312
Got key oranges which maps to value 525
Got key pears which maps to value 217
['apples', 'bananas', 'oranges', 'pears']
Got key apples
Got key bananas
Got key oranges
Got key pears

Funções para dicionários
my_dict = {
    "1": "a",
    "2": "b",
    "3": "c"
}

my_dict.items()  # dict_items([('1', 'a'), ('3', 'c'), ('2', 'b')])
my_dict.keys()   # dict_keys(['1', '3', '2'])
my_dict.values() # dict_values(['a', 'c', 'b'])
"""

"""
Programando Com Estilo
É muito importante deixar o programa fácil de ler pois, na prática, programas são lidos e modificados com muito mais frequência com que são escritos.

Vamos falar mais sobre estilo a medida que nossos programas se tornem mais complexos, mas alguns pontos já podem ser considerados:

use 4 espaços para tabulação

imports devem ser colocados no início do arquivo

a definição de funções devem ser separadas por duas linhas em branco

mantenha a definição de funções juntas no início do arquivo.

mantenha os comandos do programa principal (ou nível mais alto), incluindo as chamadas de funções, juntas no final do arquivo.

"""

# http://excript.com/python/funcoes-dicionarios.html

# Como Pensar Como um Cientista da Computação
# https://panda.ime.usp.br/panda/static/pensepy/index.html

"""
https://cadernoscicomp.com.br/tutorial/introducao-a-programacao-em-python-3/funcoes-print-input-e-o-metodo-format/
s = 'Adoro Python'
s1 = "{0:>20}".format(s)
# alinha a direita com 20 espaços em branco
print(s1)
s2 = "{0:#>20}".format(s)
# alinha a direita com 20 símbolos #
print(s2)
s3 = "{0:^20}".format(s)
# alinha ao centro usando 10 espaços em branco a esquerda e 10 a direita
print(s3)
s4 = "{0:#^20}".format(s)
# alinha ao centro usando 10 # em branco a esquerda e 10 a direita
print(s4)
# imprime só as primeiras cinco letras
print("{0:.5}".format(s)) 
"""


def main():
    print ("main - principal")

if __name__ == '__main__':
    main ()
    print ("\n" + "*" * 100)
