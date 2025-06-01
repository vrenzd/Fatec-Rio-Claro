idade = int(input('Digite sua idade: '))
cartao_estudante = input('Tem carteira de estudante (sim ou não): ').upper()
tarifa_normal = 4.50

if idade < 6 or idade > 65:
    print('Grátis')
elif cartao_estudante == 'S':
    tarifa = (tarifa_normal * 0.5)
    print(f'O estudante com 50% de desconto, pagará um total de R${tarifa:.2f}')
else:
    tarifa = tarifa_normal
    print(f'Sua tarifa normal é R${tarifa:.2f}')
