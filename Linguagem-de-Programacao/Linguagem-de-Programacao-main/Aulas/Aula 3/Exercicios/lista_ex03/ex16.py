salario_bruto = float(input('Informe seu salário: R$'))
aliquota = 0

if salario_bruto < 1900:
    print('Isento')
elif 1900 <= salario_bruto < 2800:
    aliquota = 0.075 * salario_bruto
    salario_liquido =  salario_bruto - aliquota
    print(f'O salário líquido será de R${salario_liquido:.2f}')
elif 2800 <= salario_bruto < 3700:
    aliquota = 0.15 * salario_bruto
    salario_liquido = salario_bruto - aliquota
    print(f'O salário líquido será de R${salario_liquido:.2f}')
elif 3700 <= salario_bruto < 4600:
    aliquota = 0.225 * salario_bruto
    salario_liquido = salario_bruto - aliquota
    print(f'O salário líquido será de R${salario_liquido:.2f}')
elif salario_bruto >= 4600:
    aliquota = 0.275 * salario_bruto
    salario_liquido = salario_bruto - aliquota
    print(f'O salário líquido será de R${salario_liquido}')
else:
    print('Valor inválido! Digite novamente.')
