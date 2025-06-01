codigo = int(input('Qual código do seu cargo'))

if codigo == 1:
    cargo = 'Escrituário'
    sal_base = 2500
    beneficio = 300
    imposto = ((sal_base + beneficio) - (sal_base + beneficio * 0.08))
    salario_liquido = sal_base + beneficio - imposto
    print(f'O cargo de {cargo} tem um salário liquído de R${salario_liquido:.2f}')
elif codigo == 2:
    cargo = 'Secretario'
    sal_base = 3200
    beneficio = 450
    imposto = ((sal_base + beneficio) - (sal_base + beneficio * 0.1))
    salario_liquido = sal_base + beneficio - imposto
    print(f'O cargo de {cargo} tem um salário liquído de R${salario_liquido:.2f}')
elif codigo == 3:
    cargo = 'Caixa'
    sal_base = 3800
    beneficio = 600
    imposto = ((sal_base + beneficio) - (sal_base + beneficio * 0.12))
    salario_liquido = sal_base + beneficio - imposto
    print(f'O cargo de {cargo} tem um salário liquído de R${salario_liquido:.2f}')

elif codigo == 4:
    cargo = 'Gerente'
    sal_base = 7500
    beneficio = 1000
    imposto = ((sal_base + beneficio) - (sal_base + beneficio * 0.15))
    salario_liquido = sal_base + beneficio - imposto
    print(f'O cargo de {cargo} tem um salário liquído de R${salario_liquido:.2f}')

elif codigo == 5:
    cargo = 'Diretor'
    sal_base = 12000
    beneficio = 2000
    imposto = ((sal_base + beneficio) - (sal_base + beneficio * 0.2))
    salario_liquido = sal_base + beneficio - imposto
    print(f'O cargo de {cargo} tem um salário liquído de R${salario_liquido:.2f}')


