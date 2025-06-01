idade = int(input('Qual é sua idade? '))

if idade < 14:
    print('Não pode entrar')
elif idade < 18:
    print('Pode com acompanhamento dos pais, masnão pode beber')
elif idade > 18:
    print('Pode entrar e beber')
