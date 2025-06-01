salario_atual = float(input("Digite o salário atual: R$"))

if salario_atual < 2000:
    percentual = 0.2
    bonus = salario_atual * percentual
    print(f'Bônus salarial de 20% R${bonus:.2f}')
elif 2000 <= salario_atual < 5000:
    percentual = 0.1
    bonus = salario_atual * percentual
    print(f'Bônus salarial de 10% R${bonus:.2f}')
elif salario_atual >= 5000:
    percentual = 0.05
    bonus = salario_atual * percentual
    print(f'Bônus salarial de 5% R${bonus:.2f}')
else:
    print('Sem bônus salarial')

print(f'Salário total R${salario_atual + bonus:.2f}')