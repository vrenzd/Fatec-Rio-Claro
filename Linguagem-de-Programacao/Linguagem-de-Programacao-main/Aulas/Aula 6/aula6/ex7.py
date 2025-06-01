def fatorial(n):
    x = 1
    for i in range(n, 0, -1):
        x *= i
    return x
    
n = int(input('Digite um número: '))
resultado = fatorial(n)
print(f'{n}! é o mesmo que {resultado}')
