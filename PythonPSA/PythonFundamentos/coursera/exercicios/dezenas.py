numero_inteiro = int(input("Digite um número inteiro: "))

unidades = numero_inteiro % 10

numero_inteiro = (numero_inteiro - unidades)/10

dezenas = int(numero_inteiro % 10)

print("O dígito das dezenas é " + str(dezenas))   