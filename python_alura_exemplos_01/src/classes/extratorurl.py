import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

if __name__ == '__main__':
    url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
    extrator_url = ExtratorURL(url)

    VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
    moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
    moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
    quantidade = extrator_url.get_valor_parametro("quantidade")
   
# url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
# extrator_url = ExtratorURL(url)
# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(valor_quantidade)

"""
Exemplos de URLs válidas:
    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio

Exemplos de URL inválidas:
    https://bytebank/cambio
    http://bytebank.naoexiste/cambio
    ht:bytebank.naoexiste/cambio
"""
        """

        
05
Validando nossa URL com RegEx
PRÓXIMA ATIVIDADE

Replay
Mute
Current Time 11:47
/
Duration 11:47
2xPlayback Rate
Open quality selector menuPicture-in-Picture
Open Theater Mode
Fullscreen
Transcrição
[00:00] Já aprendemos um pouco mais sobre expressões regulares e como podemos utilizá-las para extrair um padrão dentro de uma string.

[00:09] Aqui no nosso caso, o nosso padrão era o CEP, onde ele tem cinco dígitos, um hífen e mais três dígitos, e conseguimos extrair esse CEP diretamente de um endereço, ou seja, de um texto inteiro.

[00:21] Agora nós queremos utilizar essa ferramenta de expressões regulares para encontrar padrões para verificar se a nossa URL segue um determinado padrão. Como assim?

[00:31] Olhando aqui uma lista que eu tenho, nesse bloco de notas, eu coloquei só alguns exemplos de URLs que seriam consideradas válidas. Por exemplo, “bytebank.com/cambio”, “bytebank.com.br/cambio” também ou então iniciando com ‘www’, também seria uma URL válida, iniciando com ‘http’ ou ‘https’.

Exemplos de URLs válidas:

bytebank.com/cambio
bytebank.com.br/cambio
www.bytebank.com/cambio
www.bytebank.com.br/cambio
http://www.bytebank.com/cambio
http://www.bytebank.com.br/cambio
https://www.bytebank.com/cambio
https://www.bytebank.com.br/cambio
Exemplos de URLs inválidas:

https://bytebank/cambio
https://bytebank.naoexiste/cambio
ht://bytebank.naoexiste/cambio
[00:51] E aqui eu também coloquei alguns exemplos de URLs inválidas. Por exemplo, “https://bytebank/cambio”, isso não é válido porque ele precisa ter um “.com” ou “.com.br” depois do nome do domínio bytebank. Ou então “http://bytebank.naoexiste/cambio”, onde esse “naoexiste” também não faz sentido, ele realmente não existe, teria que ser “.com” ou “.com.br”.

[01:17] E até aqui outro exemplo de uma URL inválida, que é “ht:bytebank”. Então ou começa com ‘http’ ou ‘https’ ou não começa com nada, a nossa URL não pode começar com “ht:” ou “ht:” e só uma barra, tem que seguir esse certo padrão para ser válida.

[01:36] E até o momento, a nossa validação, voltando para a nossa classe principal, o extrator_url(), ela não verifica nada disso, ela só verifica se a nossa URL está vazia ou não. E agora queremos utilizar expressões regulares para fazer a nossa validação abordar todos aqueles casos.

[01:53] Nós poderíamos até tentar fazer isso utilizando if e else, mas ia ficar um código completamente confuso e poluído, porque eu teria que ficar verificando if “http” ou “https://”, com ou sem “.com.br”, então seriam diversas condições, nosso código não ia ficar nem um pouco legível, ia ficar muito mais difícil de manter também, caso alguma coisa mudasse no padrão da nossa URL.

[02:16] E para começarmos utilizando e verificando essa validação através de formato, eu vou criar um novo arquivo chamado "validador_url", você clica no menu superior, à esquerda, em “File > New > Python File”, “validador_url” e vamos aqui começar construindo o nosso padrão baseado naquelas URLs que vimos.

[02:35] Para facilitar, posso copiar do nosso bloco de notas e colocar no arquivo para termos isso como referência usando #. Perfeito. Eu deixei aqui no código, comentado, para podermos ir seguindo.

[02:46] E para construir o nosso padrão que vamos utilizar para validar a nossa URL, vamos pegar o exemplo mais completo, que seria esse último aqui, “https://www.bytebank.com.br/cambio” e vamos nos basear nesse padrão.

[03:05] Vou deixá-lo aqui embaixo, para ficar mais fácil para seguirmos. Vamos centralizar um pouco o texto aqui na tela, ótimo. Esse é o padrão que nós queremos representar em uma RegEx. Então vamos começar.

[03:18] Vamos criar uma variável padrao_url() e, lembrando, sempre em RegEx vai seguir três passos, que são: compilar um padrão, comparar esse padrão com uma string e verificar se isso retornou alguma combinação, se esse padrão foi encontrado.

[03:34] Primeira coisa que temos que fazer aqui é importar o módulo import re do Python, de expressões regulares, e começar a escrever o nosso padrão aqui. Qual é a primeira coisa que pode ter? Ele pode começar com https ou não, então já vamos criar o seguinte aqui. Quer dizer, tem que declarar uma string. padrao_url = '(https://)'.

[03:58] E você pode perceber que eu estou usando parênteses ao invés de colchetes, por quê? Quando utilizamos colchetes, por exemplo, [abc], eu estou dizendo que esse conjunto da minha expressão regular pode ter qualquer um desses caracteres aqui dentro, ou pode ser ‘a’ ou pode ser ‘b’ ou pode ser ‘c’.

import re

padrao_url = '(https://) [abc]'COPIAR CÓDIGO
[04:17] Quando eu utilizo parênteses, eu estou falando que aquele conjunto tem que ser exatamente aqueles caracteres, ou seja, se eu coloco (abc), a nossa string a ser comparada com o padrão teria que possuir exatamente ‘abc’ e não só um desses caracteres. Estamos utilizando parênteses porque eu estou falando: “Ele tem que começar com https”.

import re

padrao_url = '(https://) (abc)'COPIAR CÓDIGO
[04:46] Mas já sabemos que o https é opcional, então eu posso colocar um ponto de interrogação aqui, dizendo que minha string começa com ‘https’ ou não, a minha URL para ser válida, padrao_url = '(https://)?'.

[04:58] E agora vamos para o ‘www’. De novo eu posso colocar entre parênteses, (www.), ponto porque se tem ‘www’, ele tem que ter um ponto logo depois, antes do nome do domínio, no caso, ‘bytebank’.

[05:10] E a mesma coisa, eu coloco outro ponto de interrogação para dizer que esse conjunto pode aparecer ou não. E se aparecer, ele tem que ser exatamente “www.”. Em seguida, para a nossa URL ser válida, ela tem que ser chamada bytebank, o nosso domínio, padrao_url = '(https://)?(www.)?bytebank'.

[05:27] E o interessante é que podemos ou não utilizar parênteses aqui, porque eu só quero esse texto, não vou colocar nenhum quantificador, eu não vou colocar um ponto de interrogação depois ou algo assim, então eu posso só escrever bytebank.com, porque no mínimo tem que ter “.com”, e mais uma vez vamos ter o “.br” opcional, podendo ter ou não esse conjunto, padrao_url = '(https://)?(www.)?bytebank.com(.br)?'.

[05:49] E agora nós seguimos como? Com uma barra /, que é a minha barra que separa a minha página do meu domínio, e escrito cambio. padrao_url = '(https://)?(www.)?bytebank.com(.br)?/cambio' E nesse padrão aqui nós já conseguimos abordar algumas coisas, já conseguimos ver se tem ‘https’ ou não, se tem ‘www‘ ou não.

[06:09] Agora, o ‘https’ é um pouco mais complicado do que isso, por quê? Porque ele pode existir assim ‘https’, mas ele também pode ser ‘http’ apenas.

[06:20] O que eu posso fazer aqui? Eu posso, mais uma vez, colocar um parêntese, e aqui tanto faz colocar parênteses ou colchetes, porque eu vou estar falando somente do ‘s’, de um caractere só, e um ponto de interrogação, falando que ou tem ‘https’ ou tem só ‘http’, mas se tiver qualquer um dos dois, vai ter que ter depois o dois pontos barra, barra ’:// ’. E com isso eu já consegui abordar diversos cenários da minha URL para verificar se ela é válida ou não. padrao_url = '(http(s)?://)?(www.)?bytebank.com(.br)?/cambio'.

[06:50] Agora o próximo passo, tendo o nosso padrão construído, é verificarmos e vermos se ele combina com alguma outra string, ou seja, fazemos padrao_url.. No exercício anterior tínhamos utilizado o search() e aqui nós passávamos uma string para esse search().

[07:08] O search() vai buscar dentro de uma string se aquele padrão foi encontrado. Só que no nosso caso, eu não quero verificar se a minha string inteira possui uma URL dentro dela ou não, eu quero verificar se ela é exatamente aquele padrão, se ela bate exatamente com aquilo. E para isso, ao invés de usar o método search() do meu objeto de padrão, o pattern, eu tenho que utilizar o método .match(), padrao_url.match (' ').

import re

padrao_url = '(http(s)?://)?(www.)?bytebank.com(.br)?/cambio'
padrao_url.match('....')COPIAR CÓDIGO
[07:34] E aqui está falando que está dando errado por quê? Porque, olha só, não existe o atributo match() para a classe string. Porque aqui eu esqueci de compilar o meu padrão. Então eu tenho o meu padrão URL como uma string, só que eu tenho que compilar essa string, ou seja, eu tenho que chamar o re.compile() passando essa string, padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio').

[07:52] E agora a nossa IDE parou de apontar um erro aqui porque o match é um método do objeto pattern, que é o retornado pelo compile.

[08:03] Eu quero saber se esse padrão vai dar match em uma variável chamada url, por exemplo, que eu vou declarar aqui em cima. E vou copiar essa nossa URL aqui, a https://www.bytebank.com.br/cambio, essa URL mais completa. Tenho a minha URL, tenho meu padrão da URL e fiz um match.

[08:28] E agora eu tenho que salvar esse match numa variável que eu vou chamar de match também, match = padrao_url.match(url). E nós verificamos o quê? if match, ou seja, o match retorna none quando ele não encontra nada, se ele encontrar alguma coisa, no nosso caso, se a URL que ele está buscando segue exatamente aquele padrão, ele vai retornar um objeto match, então eu posso só fazer if match.

[08:49] Ou melhor dizendo, if not match:, se não retornar, eu vou fazer o quê? raise ValueError (“A URL não é válida.”). E caso contrário, eu vou só imprimir aqui no final print (“A URL é válida”). Vamos executar esse nosso programa validador_url.py e ver o que acontece? Clicando com o botão direito, “Run validador_url”.

import re

url = 'https://www.bytebank.com.br/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL não é válida.")

print("A URL é válida")COPIAR CÓDIGO
[09:15] Ele falou: “A URL é válida”, parece que não deu erro. Vamos testar? Vamos alterar a nossa URL aqui, para, por exemplo, htps, o que não seria válido, e vamos executar mais uma vez. Deu um erro, “A URL não é válida”. Interessante.

[09:31] Será que se eu tirar o htps daqui ela vai ser válida? Isso aqui era válido, www.bytebank.com.br/cambio. “Run”. Perfeito, a URL é válida.

[09:44] Agora temos uma validação com apenas três, quatro linhas de código, muito mais robusta do que aquela outra que só verificava se a nossa URL era vazia ou não.

[09:53] E basta agora copiarmos esse trecho de código, onde eu defino meu padrão, compilo meu padrão e verifico se encontrou um match ou não, para o nosso método valida_url() na nossa classe original.

[10:06] Então logo depois de verificar se a URL é vazia ou não eu posso fazer o meu padrão, compilando de acordo com um padrão de URL, e aqui só faltou eu importar o módulo re. E isso nós fazemos lá em cima, que é uma boa prática, import re.

[10:26] E agora eu vou executar o meu programa extrator_url.py todo uma vez, o programa original, para ver se ele continua funcionando como esperado.

import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)COPIAR CÓDIGO
[10:32] Beleza, retornou 100, que era o parâmetro que estávamos buscando aqui. E eu vou alterar, por exemplo, finge que estamos em uma página inválida aqui, eu vou botar a página ‘xyz’, alterando aqui a nossa URL para bytebank.com/xyz. E vamos executar. Ele deu um erro falando: “A URL não é válida”, como esperado. Vamos voltar para a nossa página de câmbio, perfeito.

[10:58] Com isso, nós melhoramos muito a nossa validação da URL, aprendemos que podemos utilizar RegEx para isso. Aprendemos também, dentro de RegEx ainda, a questão de utilizar parênteses ao invés de colchetes, para quando eu quero descrever um conjunto de caracteres todos aparecendo ao invés de dizer todas as opções de caracteres que podem aparecer.

[11:17] E também aprendemos o novo método do objeto pattern, que é o match(), que vai verificar se a sua string bate exatamente com aquele padrão.

[11:25] Lembrando, nós utilizamos o search() quando queremos buscar um padrão dentro de uma string inteira e o match() quando queremos verificar se a nossa string inteira bate com aquele padrão.

[11:36] Na próxima aula nós vamos aprender um pouco mais sobre os métodos especiais do Python para deixar essa nossa classe de extração de URL ainda mais elegante, e eu te vejo lá.

        """