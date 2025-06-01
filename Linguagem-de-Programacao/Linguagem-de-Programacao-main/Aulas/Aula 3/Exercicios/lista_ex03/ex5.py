n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

soma = n1 + n2

if n1 > n2:
    print(f"O maior número é {n1}")
elif n2 > n1:
    print(f"O maior número é {n2}")
else:
    print("Os números são iguais")
