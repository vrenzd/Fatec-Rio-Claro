peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso normal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 35:
    print('Obesidade Grau I')
elif 35 <= imc < 40:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III (mórbida)')
