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
# # 5 d??gitos + h??fen (opcional) + 3 d??gitos
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
# # 5 d??gitos + h??fen (opcional) + 3 d??gitos
# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
# busca = padrao.search(endereco)  # Match
# if busca:
#     cep = busca.group()
#     print(cep)

#######################################################################

# endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"
# import re  # Regular Expression -- RegEx
#
# # 5 d??gitos + h??fen (opcional) + 3 d??gitos
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
#     raise ValueError("A URL n??o ?? v??lida.")
#
# print("A URL ?? v??lida")

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
Padr??es Simples
Vamos come??ar por aprender sobre as express??es regulares mais simples poss??veis. Como as express??es regulares s??o usadas para operar em strings, vamos come??ar com a tarefa mais comum: de correspond??ncia caracteres.

Para uma explica????o detalhada da ci??ncia da computa????o referente a express??es regulares (aut??matos finitos determin??sticos e n??o-determin??stico), voc?? pode consultar a praticamente qualquer livro sobre a escrita de compiladores.

Caracteres Correspondentes
A maioria das letras e caracteres simplesmente ir??o corresponder entre si. Por exemplo, a express??o regular teste ir?? combinar com a string teste totalmente. (Voc?? pode habilitar o modo de mai??sculas e min??sculas que faria com que a RE corresponder com Test ou TEST tamb??m; veremos mais sobre isso mais adiante.)

H?? exce????es a essa regra, alguns caracteres s??o metacaracteres especiais, e n??o se correspondem. Em vez disso, eles sinalizam que alguma coisa fora do normal deve ser correspondida, ou eles afetam outras partes da RE, repetindo-as ou alterando seus significados. Grande parte deste documento ?? dedicada ?? discuss??o de v??rios metacaracteres e o que eles fazem.

Aqui est?? a lista completa de metacaracteres; seus significados ser??o discutidos ao longo deste documento.

. ^ $ * + ? { } [ ] \ | ( )
O primeiro metacaractere que vamos estudos ?? o [ e o ].  Eles s??o usados para especificar uma classe de caracteres, que ?? um conjunto de caracteres que voc?? deseja combinar. Caracteres podem ser listados individualmente ou um range de caracteres pode ser indicado dando dois caracteres e separando-os por um '-'.  Por exemplo, [abc] ir?? encontrar qualquer caractere a, b, ou c; isso ?? o mesmo que escrever [a-c], que usa um range para expressar o mesmo conjunto de caracteres, Se voc?? deseja encontrar apenas letras min??sculas, sua RE seria [a-z].

Metacaracteres n??o s??o ativos dentro de classes. Por exemplo, [akm$] ir?? combinar com qualquer dos caracteres 'a', 'k', 'm', or '$'; '$' ?? normalmente um metacaractere, mas dentro de uma classe de caracteres ele perde sua natureza especial.

Voc?? pode combinar os caracteres n??o listados na classe complementando o conjunto. Isso ?? indicado pela inclus??o de um '^' como o primeiro caractere da classe. Por exemplo, [^5] combinar?? a qualquer caractere, exceto '5'. Se o sinal de intercala????o aparecer em outro lugar da classe de caracteres, ele n??o ter?? um significado especial. Por exemplo: [5^] corresponder?? a um '5' ou a '^'.

Talvez o metacaractere mais importante ?? a contrabarra, \. Como as strings literais em Python, a barra invertida pode ser seguida por v??rios caracteres para sinalizar v??rias sequ??ncias especiais. Ela tamb??m ?? usada para escapar todos os metacaracteres, e assim, voc?? poder combin??-los em padr??es; por exemplo, se voc?? precisa fazer correspond??ncia a um [ ou \, voc?? pode preced??-los com uma barra invertida para remover seu significado especial: \[ ou \\.

Algumas das sequ??ncias especiais que come??am com '\' representam conjuntos de caracteres predefinidos que s??o frequentemente ??teis, como o conjunto de d??gitos, o conjunto de letras ou o conjunto de qualquer coisa que n??o seja espa??o em branco.

Vejamos um exemplo: \w corresponde a qualquer caractere alfanum??rico. Se o padr??o regex for expresso em bytes, isso ?? equivalente ?? classe [a-zA-Z0-9_]. Se o padr??o regex for uma string, \w combinar?? todos os caracteres marcados como letras no banco de dados Unicode fornecido pelo m??dulo unicodedata. Voc?? pode usar a defini????o mais restrita de \w em um padr??o de string, fornecendo o sinalizador re.ASCII ao compilar a express??o regular.

A lista a seguir de sequ??ncias especiais n??o est?? completa. Para obter uma lista completa das sequ??ncias e defini????es de classe expandidas para padr??es de Strings Unicode, veja a ??ltima parte de Sintaxe de Express??o Regular na refer??ncia da Biblioteca Padr??o. Em geral, as vers??es Unicode correspondem a qualquer caractere que esteja na categoria apropriada do banco de dados Unicode.

\d
corresponde a qualquer d??gito decimal, que ?? equivalente ?? classe [0-9].

\D
corresponde a qualquer caractere n??o-d??gito, o que ?? equivalente ?? classe [^0-9].

\s
corresponde a qualquer caractere espa??o-em-branco, o que ?? equivalente ?? classe [\t\n\r\f\v].

\S
corresponde a qualquer caractere n??o-espa??o-branco, o que ?? equivalente ?? classe [^\t\n\r\f\v].

\w
corresponde a qualquer caractere alfanum??rico, o que ?? equivalente ?? classe [azA-Z0-9_].

\W
corresponde a qualquer caractere n??o-alfanum??rico, o que ?? equivalente ?? classe [^a-zA-Z0-9_].
"""
