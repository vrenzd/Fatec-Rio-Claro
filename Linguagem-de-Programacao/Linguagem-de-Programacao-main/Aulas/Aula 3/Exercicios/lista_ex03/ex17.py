valor_saque = int(input('Digite o valor de saque: R$'))
cedula100 = 0
cedula50 = 0
cedula20 = 0
cedula10 = 0

while True:
    if valor_saque >= 100:
        cedula100 += 1
        valor_saque -= 100
    elif valor_saque >= 50:
        cedula50 += 1
        valor_saque -= 50
    elif valor_saque >= 20:
        cedula20 += 20
        valor_saque -= 20
    elif valor_saque >= 10:
        cedula10 += 10
        valor_saque -= 10
    else:
        break

print(f'O valor de R${valor_saque:.2f} precisará de\n{cedula100} cédula de R$100\n{cedula50} cédula de 50$\n{cedula20} cédula de 20$\n{cedula10} cédulas de R$10')

