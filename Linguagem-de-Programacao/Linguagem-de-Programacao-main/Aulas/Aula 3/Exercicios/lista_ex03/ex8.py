n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 + n2 < n3 or n1 + n3 < n2 or n2 + n3 < n1:
    if n1 == n2 == n3:
        print("Formam um triângulo equilátero")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("Formam um triângulo isósceles")
    else:
        print("Formam um triângulo escaleno")
else:
    print("Não formam um triângulo")
    