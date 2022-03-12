"""
Opinião do instrutor

Temos o costume de usar o sufixo Factory nas nossas classes que são fábricas.

O prefixo get também é bastante usado.

Muitas vezes vale a pena seguir a convenção, já que, dessa forma, 
outros desenvolvedores entenderão mais facilmente o código.

Factory Method em Python
O Factory method é um padrão de projeto criacional, 
que resolve o problema de criar objetos de produtos sem especificar 
suas classes concretas.

O Factory Method define um método, que deve ser usado para criar objetos em vez da chamada direta ao construtor (operador new). As subclasses podem substituir esse método para alterar a classe de objetos que serão criados.

Se você não conseguir descobrir a diferença entre os padrões Factory, Factory Method e Abstract Factory, leia nossa Comparação Factory.

Uso do padrão em Python
Complexidade: 

Popularidade: 

Exemplos de uso: O padrão Factory Method é amplamente utilizado no código Python. É muito útil quando você precisa fornecer um alto nível de flexibilidade para seu código.

Identificação: Os métodos fábrica podem ser reconhecidos por métodos de criação, que criam objetos de classes concretas, mas os retornam como objetos de tipo ou interface abstrata.

Exemplo conceitual
Este exemplo ilustra a estrutura do padrão de projeto Factory Method. 
Ele se concentra em responder a estas perguntas:

De quais classes ele consiste?
Quais papéis essas classes desempenham?
De que maneira os elementos do padrão estão relacionados?

===============
Geralmente usamos um builder quando precisamos passar diversas informações para a lógica que monta o objeto. No caso da Nota Fiscal, passamos nome, ítens, etc.

Usamos uma fábrica quando temos que isolar o processo de criação de um objeto em um único lugar. Essa fábrica pode descobrir como criar o objeto dentro dela própria, mas geralmente ela não precisa de muitas informações para criar o objeto.

# -*- coding: utf-8 -*-
import MySQLdb

class Connection_factory(object):

    def get_connection(self):

        return MySQLdb.connect(host="localhost", 
            user='root', 
            passwd='',
            db='alura')
"""