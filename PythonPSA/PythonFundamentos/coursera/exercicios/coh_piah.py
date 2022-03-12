#coding:utf-8
"""
#Programa
Prólogo
Neste último exercício da Parte 1, iremos praticar não só o que vimos até agora no curso mas também outra habilidade importante de um programador: utilizar e interagir com código escrito por terceiros. Aqui, você não irá implementar o seu programa do zero. Você irá partir de um programa já iniciado e irá completá-lo. Na verdade, esse é o caso mais comum na indústria de software, onde muitos desenvolvedores trabalham colaborativamente em um mesmo programa.

Introdução 
Manuel Estandarte é monitor na disciplina Introdução à Produção Textual I na Universidade de Pasárgada (UPA). Durante o período letivo, Manuel descobriu que uma epidemia de COH-PIAH estava se espalhando pela UPA. Essa doença rara e altamente contagiosa faz com que indivíduos contaminados produzam, involuntariamente, textos muito semelhantes aos de outras pessoas. Após a entrega da primeira redação, Manuel desconfiou que alguns alunos estavam sofrendo de COH-PIAH. Manuel, preocupado com a saúde da turma, resolveu buscar um método para identificar os casos de COH-PIAH. Para isso, ele necessita da sua ajuda para desenvolver um programa que o auxilie a identificar os alunos contaminados.

Detecção de autoria
Diferentes pessoas possuem diferentes estilos de escrita; por exemplo, algumas pessoas preferem sentenças mais curtas, outras preferem sentenças mais longas. Utilizando diversas estatísticas do texto, é possível identificar aspectos que funcionam como uma “assinatura” do seu autor e, portanto, é possível detectar se dois textos dados foram escritos por uma mesma pessoa. Ou seja, essa “assinatura” pode ser utilizada para detecção de plágio, evidência forense ou, neste caso, para diagnosticar a grave doença COH-PIAH.

Traços linguísticos
Neste exercício utilizaremos as seguintes estatísticas para detectar a doença:

Tamanho médio de palavra: Média simples do número de caracteres por palavra.
Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.
Tamanho médio de sentença: Média simples do número de caracteres por sentença.
Complexidade de sentença: Média simples do número de frases por sentença.
Tamanho médio de frase: Média simples do número de caracteres por frase.
Funcionamento do programa
A partir da assinatura conhecida de um portador de COH-PIAH, seu programa deverá receber diversos textos e calcular os valores dos diferentes traços linguísticos desses textos para compará-los com a assinatura dada. Os traços linguísticos que seu programa deve utilizar são calculados da seguinte forma:

Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale  \frac{4}{5} = 0.8  
5
4
​
 =0.8
Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale  \frac{3}{5} = 0.6  
5
3
​
 =0.6
Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).
Complexidade de sentença é o número total de frases divido pelo número de sentenças.
Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto  (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
Após calcular esses valores para cada texto, você deve compará-los com a assinatura fornecida para os infectados por COH-PIAH. O grau de similaridade entre dois textos,  a a e  b b, é dado pela fórmula:

 S_{ab} = \frac{\sum_{i=1}^6 || f_{i,a} - f_{i,b} ||}{6} S 
ab
​
 = 
6
∑ 
i=1
6
​
 ∣∣f 
i,a
​
 −f 
i,b
​
 ∣∣
​
 

Onde:

 S_{ab} S 
ab
​
  é o grau de similaridade entre os textos  a a e  b b;
 f_{i,a} f 
i,a
​
  é o valor de cada traço linguístico  i i no texto  a a; e
 f_{i,b} f 
i,b
​
  é o valor de cada traço linguístico  i i no texto  b b.
No nosso caso, o texto  b b não é conhecido, mas temos a assinatura correspondente: a assinatura de um aluno infectado com COH-PIAH. Ou seja, sabemos o valor de  f_{i,b} f 
i,b
​
  que é dado como valor de entrada do programa. 

Caso você não esteja acostumado com a notação matemática, podemos destrinchar essa fórmula da seguinte maneira: 

Para cada traço linguístico  i i (tamanho médio da palavra, relação type-token etc.) se quer a diferença entre o valor obtido em cada texto dado ( a a) e o valor típico do texto de uma pessoa infectada ( b b):  f_{i, a} - f_{i, b} f 
i,a
​
 −f 
i,b
​
 

Dessa diferença se toma o módulo ( || \ldots || ∣∣…∣∣), lembre-se da função abs do python.

Somamos os resultados dos 6 traços linguísticos (\sum_{i=1}^6∑ 
i=1
6
​
 )

E por final dividimos por 6 (  \frac{x}{6} 
6
x
​
 )

Perceba que quanto mais similares  a a e  b b forem, menor  S_{ab} S 
ab
​
  será. Para cada texto, você deve calcular o grau de similaridade com a assinatura do portador de COH-PIAH e, no final, exibir qual texto mais provavelmente foi escrito por algum aluno infectado (ou seja, o texto com assinatura mais similar à assinatura dada).

Exemplo:

123456789101112131415161718192021
$ > python3 coh_piah.py

Bem-vindo ao detector automático de COH-PIAH.
Informe a assinatura típica de um aluno infectado:

Entre o tamanho médio de palavra: 4.51
Entre a relação Type-Token: 0.693
Entre a Razão Hapax Legomana: 0.55
Entre o tamanho médio de sentença: 70.82
Entre a complexidade média da sentença: 1.82

Funções de suporte
Para facilitar seu trabalho, fornecemos para você um esqueleto do programa completo como base. Use-o! As funções definidas nele devem ser utilizadas no seu programa; algumas já estão implementadas, outras devem ser implementadas por você (conforme indicado pelo comentário "IMPLEMENTAR"). Sinta-se livre para criar funções adicionais, caso necessário.

12345678910111213141516171819202122232425262728293031323334353637383940
import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))

Dica: não se preocupe com os detalhes de implementação das funções pré-prontas do esqueleto, como "separa_sentenca()", "separa_frase()" etc. nem com as definições exatas de frase e sentença. Essas funções já cuidam disso para você, e podem ser pensadas como "caixas pretas": você pode utilizá-las sabendo o que recebem e o que devolvem, mas não é necessário saber sobre os seus detalhes internos. Além de isso ser muito comum ao programar em equipe, usando essas funções você vai fazer o cálculo da maneira esperada pelo corretor automático.

Cuidado: A função le_textos() considera que um "texto" é uma linha de texto, ou seja, não é possível inserir parágrafos separados. Se você digitar algum "enter", a função vai entender que você está começando um novo texto. Preste especial atenção a isso se usar "copiar/colar" para inserir os textos! Note também que, no cálculo de similaridade, é preciso encontrar o valor absoluto de cada uma das diferenças.

Exemplo de Assinatura
Um passo importante para seu programa é calcular a assinatura dos textos corretamente. Para testar se sua função calcula_assinatura()  está correta, deixamos aqui um exemplo de execução:

123
>texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza
Concluindo
Basicamente, sua tarefa é implementar corretamente as seguintes funções:  

compara_assinatura(as_a, as_b)
calcula_assinatura(texto)
avalia_textos(textos, ass_cp)
Usando o esqueleto que oferecemos acima e implementando essas 3 funções, seu detector de plágio estará completo e você poderá submetê-lo ao corretor automático. Caso o corretor automático aponte erros, tente ler com bastante cuidado e atenção a mensagem fornecida por ele, pois ela normalmente ajuda a identificar o erro.   

Boa sorte! Não desista! 

Sabemos que é um desafio, mas você vai aprender muito com ele. 

Pense no prazer que você vai sentir quando sua solução final for aceita!!!   
"""

import re
import math


def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def calcula_tamanho_medio_palavra(palavras):
    total_palavras = len(palavras)
    somatorio = 0
    for i in range(len(palavras)):
        somatorio = somatorio + len(palavras[i])
    return somatorio / total_palavras


def calcula_relacao_type_token(palavras):
    total_palavras = len(palavras)
    num_palavras_diferentes = n_palavras_diferentes(palavras)
    return num_palavras_diferentes / total_palavras


def calcula_razao_hapax_legomana(palavras):
    total_palavras = len(palavras)
    num_palavras_diferentes = n_palavras_unicas(palavras)
    return num_palavras_diferentes / total_palavras


def total_caracteres_delimitadores_fora_sentences(palavras):
    caracteres = ['.', '!', '?']
    total_caracteres = 0;
    print("total_caracteres_delimitadores_fora_sentences:", palavras)
    for i in range(len(palavras)):
        if palavras[i].find('.') >= 0 or palavras[i].find("!") >= 0 or palavras[i].find("?") >= 0:
            total_caracteres = total_caracteres + 1
    print("total_caracteres: ", total_caracteres)
    return total_caracteres


def calcula_tamanho_medio_sentencas(sentencas, palavras):
    total_sentencas = len(sentencas)
    return len(palavras) / total_sentencas


def calcula_complexidade_sentencas(sentencas, frases):
    total_sentencas = len(sentencas)
    total_frases = len(frases)
    return total_frases / total_sentencas


def total_caracteres_delimitadores_fora_frases(palavras):
    total_caracteres = 0;
    for i in range(len(palavras)):
        for j in range(len(palavras[i])):
            if palavras[i].find(',') >= 0 or palavras[i].find(":") >= 0 or palavras[i].find(";") >= 0:
                total_caracteres = total_caracteres + 1
    return total_caracteres


def calcula_tamanho_medio_frases(frases, palavras):
    total_frases = len(frases)
    return total_caracteres_delimitadores_fora_frases(palavras) / total_frases


def compara_assinatura(as_a, as_b):
    sum = 0
    for i in range(6):
        sum = sum + math.fabs(as_a[i] - as_b[i])

    return sum / 6


def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []
    for i in range(len(sentencas)):
        temp_frases = separa_frases(sentencas[i])
        for j in range(len(temp_frases)):
            frases.append(temp_frases[j])

    for i in range(len(frases)):
        temp_palavras = separa_palavras(frases[i])
        for j in range(len(temp_palavras)):
            palavras.append(temp_palavras[j])

    # Tamanho médio de palavra - wal
    wal = calcula_tamanho_medio_palavra(palavras)
    # Relação Type-Token - ttr
    ttr = calcula_relacao_type_token(palavras)
    # Razão Hapax Legomana - hlr
    hlr = calcula_razao_hapax_legomana(palavras)
    # Tamanho médio de sentença - sal
    sal = calcula_tamanho_medio_sentencas(sentencas, palavras)
    print("calculated Tamanho médio de sentença: ", sal)
    # Complexidade de sentença -  sac
    sac = calcula_complexidade_sentencas(sentencas, frases)
    # Tamanho médio de frases - pal
    pal = calcula_tamanho_medio_frases(frases, palavras)
    #print("calculated Tamanho médio de frases: ", pal)

    return [wal, ttr, hlr, sal, sac, pal]


def reconhece_autor_infectado(array):
    min = array[0]
    i = 1
    pos = 0
    while i < len(array):
        if array[i] < min:
            min = array[i]
            pos = i
        i = i + 1
    return pos


def avalia_textos(textos, ass_cp):
    array_grau_similiaridades_textos = []
    for i in range(len(textos)):
        ass_text = calcula_assinatura(textos[i])
        grau_similaridade = compara_assinatura(ass_cp, ass_text)
        array_grau_similiaridades_textos.append(grau_similaridade)
        print("calculate grau similariadade", array_grau_similiaridades_textos)

    return reconhece_autor_infectado(array_grau_similiaridades_textos)


def loadTexts():
    texts = []
    temp = "Navegadores antigos tinham uma frase gloriosa:\"Navegar é preciso; viver não é preciso\". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça."
    texts.append(temp)
    temp = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
    texts.append(temp)
    temp = "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."
    texts.append(temp)
    return texts


def loadAssinaturas():
    return [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
  
def main():
    """
    Funcao principal
    """
    texts = loadTexts()
    print("load texts...")
    ass_cp = loadAssinaturas()
    print("load assinaturas...")
    print("O autor do texto", avalia_textos(texts, ass_cp), "está infectado com COH-PIAH")
    
if __name__ == "__main__" :
    """
    Ponto de inicio
    """

    # Aciona a funcao principal
    main()
        
#Fim do programa
