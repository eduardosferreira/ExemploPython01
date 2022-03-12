n = int(input("Digite o valor de n: "))
i = 0
r = 0

while i < len(str(n)):
    r += int(str(n)[i])
    i += 1

print(r)
