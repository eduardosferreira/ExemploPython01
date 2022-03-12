"""

'>>> import this'
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

"""

'''
O Zen do Python, de Tim Peters

Belo é melhor do que feio.
Explícito é melhor do que implícito.
Simples é melhor que complexo.
Complexo é melhor do que complicado.
Plano é melhor do que aninhado.
Esparso é melhor do que denso.
A legibilidade conta.
Casos especiais não são especiais o suficiente para quebrar as regras.
Embora a praticidade supere a pureza.
Os erros nunca devem passar silenciosamente.
A menos que seja explicitamente silenciado.
Diante da ambigüidade, recuse a tentação de adivinhar.
Deve haver uma - e de preferência apenas uma - maneira óbvia de fazer isso.
Embora essa forma possa não ser óbvia no início, a menos que você seja holandês.
Agora é melhor do que nunca.
Embora nunca seja sempre melhor do que * agora *.
Se a implementação for difícil de explicar, é uma má ideia.
Se a implementação for fácil de explicar, pode ser uma boa ideia.
Os namespaces são uma ótima ideia - vamos fazer mais disso!
'''

"""

The Invent with Python Blog
Sex, 17 de agosto de 2018
O Zen do Python, explicado
Postado por Al Sweigart em python   

The Zen of Python de Tim Peters são 20 diretrizes para o design da linguagem Python. Seu código Python não precisa necessariamente seguir essas diretrizes, mas é bom mantê-las em mente. O Zen do Python é um ovo de Páscoa , ou piada oculta, que aparece se você executar import this:

>>> importe isso
O Zen do Python, de Tim Peters

Belo é melhor do que feio.
Explícito é melhor do que implícito.
Simples é melhor que complexo.
Complexo é melhor do que complicado.
Plano é melhor do que aninhado.
Esparso é melhor do que denso.
A legibilidade conta.
Casos especiais não são especiais o suficiente para quebrar as regras.
Embora a praticidade supere a pureza.
Os erros nunca devem passar silenciosamente.
A menos que seja explicitamente silenciado.
Diante da ambigüidade, recuse a tentação de adivinhar.
Deve haver uma - e de preferência apenas uma - maneira óbvia de fazer isso.
Embora essa forma possa não ser óbvia no início, a menos que você seja holandês.
Agora é melhor do que nunca.
Embora nunca seja sempre melhor do que * agora *.
Se a implementação for difícil de explicar, é uma má ideia.
Se a implementação for fácil de explicar, pode ser uma boa ideia.
Os namespaces são uma ótima ideia - vamos fazer mais disso!
NOTA: Misteriosamente, apenas 19 das diretrizes foram escritas. Guido van Rosum teria dito que o 20º aforismo que faltava é “alguma piada interna bizarra de Tim Peters”.
No final, essas diretrizes são opiniões que podem ser argumentadas a favor ou contra. Como todos os bons conjuntos de códigos morais, eles às vezes se contradizem para fornecer o máximo de flexibilidade. Aqui está minha própria interpretação desses aforismos:

Belo é melhor do que feio.
Os programadores geralmente escrevem código rapidamente sem se preocupar com a legibilidade. Embora o código não precise ser legível, o código da própria linguagem Python deve ser pensado, consistente e agradável de usar. Claro, nem todo script precisa ser bonito, e a beleza é subjetiva, mas muito da popularidade do Python é o resultado de ser tão fácil de trabalhar.

Explícito é melhor do que implícito.
“Este aforismo é autoexplicativo”, essa seria uma explicação terrível para qualquer aforismo. Da mesma forma, é melhor que o código seja prolixo e explícito. Você deve evitar ocultar a funcionalidade do código por trás de recursos de linguagem obscuros que requerem familiaridade para serem totalmente compreendidos.

Simples é melhor que complexo. Complexo é melhor do que complicado.
Esses dois aforismos nos lembram que construir qualquer coisa pode ser feito usando técnicas simples ou complexas. Com um problema simples, como construir uma gaiola, uma solução simples é melhor. Construir uma locomotiva a diesel, por outro lado, é um problema complexo que requer técnicas complexas. Mesmo se você pudesse tecnicamente fazer um motor de trem a diesel usando técnicas de casinha de pássaros, provavelmente acabaria com um arranjo complicado de Rube Goldberg de peças de casinha de pássaros que não seria a solução ideal. Prefira a simplicidade à complexidade, mas conheça os limites da simplicidade.

Plano é melhor do que aninhado.
Os programadores adoram organizar as coisas em categorias, especialmente categorias que contêm subcategorias que contêm outras subcategorias. Essas hierarquias muitas vezes não acrescentam organização tanto quanto acrescentam burocracia . É normal ter código em apenas um módulo ou classe de camada superior, em vez de dividir em vários submódulos ou subclasses. Se você faz pacotes e módulos que requerem código como import spam.eggs.bacon.ham.foo.bar, então você está tornando seu código muito complicado.

Esparso é melhor do que denso.
Os programadores geralmente como empinar tanta funcionalidade em tão pouco código possível, tais como one-liners como o seguinte: print('\n'.join("%i bytes = %i bits which has %i possible values." % (j, j*8, 256**j-1) for j in (1 << i for i in range(8)))). Embora um código como esse possa impressionar seus amigos, enfurece seus colegas de trabalho que precisam tentar entendê-lo. O código que está espalhado em várias linhas geralmente é mais fácil de ler do que uma linha densa.

A legibilidade conta.
Embora strcmp()possa obviamente significar a função de “comparação de string” para alguém que programa em C desde os anos 1970, os computadores modernos têm memória suficiente para escrever o nome completo da função. Não omita vogais de seus nomes nem escreva códigos muito concisos. O código é lido com mais frequência do que escrito, portanto, o código explícito e legível é mais importante do que o código conciso e não documentado.

Casos especiais não são especiais o suficiente para quebrar as regras. Embora a praticidade supere a pureza.
Esses dois aforismos, que vêm em conjunto, se contradizem. A programação está cheia de “melhores práticas” que os programadores devem buscar em seu código. Contornar essas práticas para um hack rápido pode ser tentador, mas pode levar a um ninho de rato de código inconsistente e ilegível. No entanto, voltar atrás para cumprir as regras pode resultar em um código altamente abstrato e ilegível. A tentativa da linguagem de programação Java de ajustar todo o código ao seu paradigma orientado a objetos freqüentemente resulta em muitos códigos clichê até mesmo para o menor programa. Andar na linha entre esses dois aforismos se torna mais fácil com a experiência. E com o tempo, você não apenas aprenderá as regras, mas também quando quebrá-las.

Os erros nunca devem passar silenciosamente. A menos que seja explicitamente silenciado.
Só porque os programadores geralmente ignoram as mensagens de erro, não significa que o programa deva parar de emiti-las. Erros silenciosos podem ocorrer quando as funções retornam códigos de erro ou em Nonevez de gerar exceções. Esses dois aforismos nos dizem que é melhor para um programa fail fasttravar do que silenciar o erro e continuar executando o programa. Os bugs que inevitavelmente acontecem mais tarde serão mais difíceis de depurar, pois estão muito longe da causa original. Embora você sempre possa escolher ignorar explicitamente os erros que seus programas causam, apenas certifique-se de fazer a escolha consciente de fazê-lo.

Diante da ambigüidade, recuse a tentação de adivinhar.
Os computadores tornaram os humanos supersticiosos: para exorcizar os demônios em nossos computadores, realizamos o ritual sagrado de desligá-los e ligá-los. Supostamente, isso resolverá qualquer problema misterioso. No entanto, os computadores não são mágicos. Se o seu código não estiver funcionando, há um motivo e apenas o pensamento crítico e cuidadoso o resolverá. Recuse a tentação de tentar soluções cegamente até que algo pareça funcionar; frequentemente, você apenas mascarou o problema, em vez de resolvê-lo.

Deve haver uma - e de preferência apenas uma - maneira óbvia de fazer isso.
Este é um aspecto contrário ao lema da linguagem de programação Perl, “Há mais de uma maneira de fazer isso!” Acontece que ter três ou quatro maneiras diferentes de escrever código que faz a mesma coisa é uma faca de dois gumes: você tem flexibilidade em como você escreve o código, mas agora você tem que aprender todas as maneiras possíveis em que ele poderia ter sido escrito em ordem para ler. Essa flexibilidade não vale o esforço 3x ou 4x necessário para aprender uma linguagem de programação.

Embora essa forma possa não ser óbvia no início, a menos que você seja holandês.
Essa linha é uma piada. Guido van Rossum, o criador e BDFL (Benevolent Dictator for Life) de Python, é holandês. No entanto, nem mesmo esse aforismo impediu o Python de incorporar três maneiras diferentes de formatar strings.

Agora é melhor do que nunca. Embora nunca seja sempre melhor do que * agora *.
Esses dois aforismos nos dizem que o código que trava ou fica preso em loops infinitos é obviamente pior do que o código que não fica. No entanto, quase certamente é melhor esperar que o programa termine do que terminá-lo muito cedo com resultados incorretos.

Se a implementação for difícil de explicar, é uma má ideia. Se a implementação for fácil de explicar, pode ser uma boa ideia.
Python se esforça para tornar o trabalho do programador mais fácil, em vez de acomodar o computador para que o programa seja executado com mais rapidez. E os programas precisam ser compreensíveis não apenas pelo programador que os escreveu, mas também por outros programadores que mantêm o código. Esses dois aforismos nos lembram que, se o código de "alto desempenho" é tão complicado a ponto de ser impossível para os programadores entenderem e depurarem, então é um código ruim. Mas, infelizmente, só porque é fácil explicar o código de um programa para outra pessoa não significa que não seja um código ruim. A programação é difícil.

Os namespaces são uma ótima ideia - vamos fazer mais disso!
Namespaces (e também escopos globais e locais) são fundamentais para evitar que nomes em um módulo ou escopo entrem em conflito com nomes em outro. Mas lembre-se também de que simples é melhor do que aninhado : por melhores que sejam, os namespaces devem ser criados apenas para evitar conflitos de nomenclatura e não para adicionar categorização desnecessária.

Como todas as opiniões sobre programação, as que escrevi aqui podem ser contestadas ou podem simplesmente ser irrelevantes para a sua situação. Discutir sobre como o código deve ser escrito raramente é tão produtivo quanto você pensa. (A menos que você esteja escrevendo um livro inteiro cheio de opiniões sobre programação.)
"""