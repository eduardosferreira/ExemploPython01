primeira_numero = float(input("Digite o primeiro numero: "))

segunda_numero = float(input("Digite o segundo numero: "))

terceira_numero = float(input("Digite o terceiro numero: "))

if ( (terceira_numero > segunda_numero) \
and (segunda_numero > primeira_numero) ):
    print("crescente")
else:
    print("não está em ordem crescente")
    