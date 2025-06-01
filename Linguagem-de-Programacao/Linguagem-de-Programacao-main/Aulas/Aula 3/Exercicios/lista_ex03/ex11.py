from random import randint
from time import sleep

usuario = randint(0, 10)

print('-=-' * 20)
print('Tente advinhar um número entre (0 e 10)')
print('-=-' * 20)

num_secreto = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(0.5)

if num_secreto > usuario:
    print('Muito alto!')
elif num_secreto < usuario:
    print('Muito baixo!')
else:
    print('Parabéns!')
        