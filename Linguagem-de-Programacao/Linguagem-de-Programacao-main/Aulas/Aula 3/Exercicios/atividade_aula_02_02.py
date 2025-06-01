nota = float(input('Digite a nota (0 a 100): '))

if nota >= 90:
    print('Aprovado com Excelência')
elif 70 <= nota < 89:
    print('Aprovado')
elif 50 <= nota < 69:
    print('Recuperação')
else:
    print('Reprovado')
