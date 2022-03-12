# #defining string and substring
# str1 = "This dress looks good; you have good taste in clothes."
# substr = "good"
#
# #occurrence of word 'good' in whole string
# count1 = str1.count(substr)
# print(count1)
#
# #occurrence of word 'good' from index 0 to 25
# count2 = str1.count(substr, 0, 25)
# print(count2)
#######################################################################
# import re
#
# # defining string
# str1 = "This dress looks good; you have good taste in clothes."
#
# #defining substring
# substr = "good"
#
# print("The original string is: " + str1)
#
# print("The substring to find: " + substr)
#
# result = [_.start() for _ in re.finditer(substr, str1)]
#
# print("The start indices of the substrings are : " + str(result))
#######################################################################

# import re
# sentence = 'Cats, rats, bats, and hats.'
#
# print('occurrence of letter a:',
#       len(re.findall('a', sentence)),
#       str(sentence).count('a'),
#       str(sentence).find('a'), str(sentence).index('a'), #obs index, gera erro qdo nao encontra, find, retorna -1
#       str(sentence).find('-sss'),
#       re.findall('a', sentence), sep=' >> ')
#
# for match in re.finditer('at', sentence):
#     s = match.start()
#     e = match.end()
#     print('String match "%s" : "%s" at %d:%d' %
#           (sentence, sentence[s:e], s, e))
#
#######################################################################

# resultado_busca = "https://www.alura.com.br/curso?curso=python"
# indice_curso = resultado_busca.find("curso")
# indice_valor = indice_curso + len("curso") + 1
# valor = resultado_busca[indice_valor:]
# print(valor)
# import re
# print([str(resultado_busca[match.start():]) for match in re.finditer('curso', resultado_busca)])

#######################################################################

# endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"
# import re  # Regular Expression -- RegEx
#
# # 5 dígitos + hífen (opcional) + 3 dígitos
# # ? SIGNIFICA que pode ou nao aparecer
#
# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789]")
# busca = padrao.search(endereco)  # Match
# if busca:
#     cep = busca.group()
#     print(cep)

#######################################################################

# endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120"
# import re  # Regular Expression -- RegEx
# # 5 dígitos + hífen (opcional) + 3 dígitos
# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
# busca = padrao.search(endereco)  # Match
# if busca:
#     cep = busca.group()
#     print(cep)

#######################################################################

# endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"
# import re  # Regular Expression -- RegEx
#
# # 5 dígitos + hífen (opcional) + 3 dígitos
#
# padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
# busca = padrao.search(endereco)  # Match
# if busca:
#     cep = busca.group()
#     print(cep)

#######################################################################

# import re  # Regular Expression -- RegEx
# endereco = "Rafaela Brasil, CPF: 718.457.190-85"
# # padrao = re.compile('[0-9]{3}[.]{1}[0-9]{3}[.]{1}[0-9]{3}[-]{1}[0123456789]{2}')
# padrao = re.compile('[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}')
# busca = padrao.search(endereco)  # Match
# if busca:
#     cpf = busca.group()
#     print(cpf)

#######################################################################

# import re
#
# resultado_busca = 'https://www.bytebank.com.br/cambio'
# padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
# match = padrao_url.match(resultado_busca)
#
# if not match:
#     raise ValueError("A URL não é válida.")
#
# print("A URL é válida")

#######################################################################

# () - o que obrigatorio Ex. (http://), deve ser obrigatorio
# ? alternativo  (http(s)?://)? aceita, https:// ou http://
# {} quantidade Ex. 3
# [] conjuntos Ex. [0-9]

#######################################################################


#######################################################################

#######################################################################

from dataclasses import replace
import re
# informacao = "Rafaela Brasil, CPF: 718.457.190-85"
informacao = 'EDUARDO DA SILVA FERREIRA |>043.458.736-22<|,|>143.258.336-99<|,|>043.458.736-22<|, '
# padrao = re.compile('(\|(>)?)?[\d]{3}[.]?[\d]{3}[.]?[\d]{3}?[-]?[\d]{2}((<)?\|)?')
# padrao = re.compile('[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}')
# padrao = re.compile('[\d]{3}[.]?[\d]{3}[.]?[\d]{3}?[-]?[\d]{2}')
padrao = re.compile('([\d]{3}[.]?){3}[-]?[\d]{2}')
contador = 0
dados = informacao
while True:
    contador += 1
    busca = padrao.search(dados)  # Match
    if busca:
        resultado_busca = busca.group()
        print(contador, resultado_busca)
        for match in re.finditer(resultado_busca, dados):
            s = match.start()
            e = match.end()
            print('String match "%s" at %d:%d replace: %s'
                  % (dados[s:e], s, e,
                     ''.join(['' if k >= s and k < e else str(
                         x) for k, x in enumerate(dados)])
                     ))
        match = padrao.match(resultado_busca) # tem que ser exatamente
        if match:
            print("Deu match .. correto....")

        dados = dados.replace(str(resultado_busca), "", 1)
    else:
        print("NAO FOI encontrado mais a INFORMACAO.")
        break
# padrao = re.compile('[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}')
# busca = padrao.search(endereco)  # Match
# if busca:
#     cpf = busca.group()
#     print(cpf)

#######################################################################

"""
Padrões Simples
Vamos começar por aprender sobre as expressões regulares mais simples possíveis. Como as expressões regulares são usadas para operar em strings, vamos começar com a tarefa mais comum: de correspondência caracteres.

Para uma explicação detalhada da ciência da computação referente a expressões regulares (autômatos finitos determinísticos e não-determinístico), você pode consultar a praticamente qualquer livro sobre a escrita de compiladores.

Caracteres Correspondentes
A maioria das letras e caracteres simplesmente irão corresponder entre si. Por exemplo, a expressão regular teste irá combinar com a string teste totalmente. (Você pode habilitar o modo de maiúsculas e minúsculas que faria com que a RE corresponder com Test ou TEST também; veremos mais sobre isso mais adiante.)

Há exceções a essa regra, alguns caracteres são metacaracteres especiais, e não se correspondem. Em vez disso, eles sinalizam que alguma coisa fora do normal deve ser correspondida, ou eles afetam outras partes da RE, repetindo-as ou alterando seus significados. Grande parte deste documento é dedicada à discussão de vários metacaracteres e o que eles fazem.

Aqui está a lista completa de metacaracteres; seus significados serão discutidos ao longo deste documento.

. ^ $ * + ? { } [ ] \ | ( )
O primeiro metacaractere que vamos estudos é o [ e o ].  Eles são usados para especificar uma classe de caracteres, que é um conjunto de caracteres que você deseja combinar. Caracteres podem ser listados individualmente ou um range de caracteres pode ser indicado dando dois caracteres e separando-os por um '-'.  Por exemplo, [abc] irá encontrar qualquer caractere a, b, ou c; isso é o mesmo que escrever [a-c], que usa um range para expressar o mesmo conjunto de caracteres, Se você deseja encontrar apenas letras minúsculas, sua RE seria [a-z].

Metacaracteres não são ativos dentro de classes. Por exemplo, [akm$] irá combinar com qualquer dos caracteres 'a', 'k', 'm', or '$'; '$' é normalmente um metacaractere, mas dentro de uma classe de caracteres ele perde sua natureza especial.

Você pode combinar os caracteres não listados na classe complementando o conjunto. Isso é indicado pela inclusão de um '^' como o primeiro caractere da classe. Por exemplo, [^5] combinará a qualquer caractere, exceto '5'. Se o sinal de intercalação aparecer em outro lugar da classe de caracteres, ele não terá um significado especial. Por exemplo: [5^] corresponderá a um '5' ou a '^'.

Talvez o metacaractere mais importante é a contrabarra, \. Como as strings literais em Python, a barra invertida pode ser seguida por vários caracteres para sinalizar várias sequências especiais. Ela também é usada para escapar todos os metacaracteres, e assim, você poder combiná-los em padrões; por exemplo, se você precisa fazer correspondência a um [ ou \, você pode precedê-los com uma barra invertida para remover seu significado especial: \[ ou \\.

Algumas das sequências especiais que começam com '\' representam conjuntos de caracteres predefinidos que são frequentemente úteis, como o conjunto de dígitos, o conjunto de letras ou o conjunto de qualquer coisa que não seja espaço em branco.

Vejamos um exemplo: \w corresponde a qualquer caractere alfanumérico. Se o padrão regex for expresso em bytes, isso é equivalente à classe [a-zA-Z0-9_]. Se o padrão regex for uma string, \w combinará todos os caracteres marcados como letras no banco de dados Unicode fornecido pelo módulo unicodedata. Você pode usar a definição mais restrita de \w em um padrão de string, fornecendo o sinalizador re.ASCII ao compilar a expressão regular.

A lista a seguir de sequências especiais não está completa. Para obter uma lista completa das sequências e definições de classe expandidas para padrões de Strings Unicode, veja a última parte de Sintaxe de Expressão Regular na referência da Biblioteca Padrão. Em geral, as versões Unicode correspondem a qualquer caractere que esteja na categoria apropriada do banco de dados Unicode.

\d
corresponde a qualquer dígito decimal, que é equivalente à classe [0-9].

\D
corresponde a qualquer caractere não-dígito, o que é equivalente à classe [^0-9].

\s
corresponde a qualquer caractere espaço-em-branco, o que é equivalente à classe [\t\n\r\f\v].

\S
corresponde a qualquer caractere não-espaço-branco, o que é equivalente à classe [^\t\n\r\f\v].

\w
corresponde a qualquer caractere alfanumérico, o que é equivalente à classe [azA-Z0-9_].

\W
corresponde a qualquer caractere não-alfanumérico, o que é equivalente à classe [^a-zA-Z0-9_].
"""
