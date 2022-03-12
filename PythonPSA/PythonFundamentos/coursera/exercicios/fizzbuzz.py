nr_numero_inteiro = int(input("Digite um numero inteiro: "))

if (nr_numero_inteiro % 3 == 0 and nr_numero_inteiro % 5 == 0):
    print("FizzBuzz")
else:
    print(str(nr_numero_inteiro))    