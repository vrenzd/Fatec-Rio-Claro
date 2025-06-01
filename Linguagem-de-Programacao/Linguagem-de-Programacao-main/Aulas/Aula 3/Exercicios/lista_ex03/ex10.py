ano = int(input('Digite o ano: '))

if (ano % 4 == 0 and ano % 4 != 100) or (ano % 400 == 0):
    print('Ano bissexto')
else:
    print('Não é bissexto')
    