nota = float(input('Digite uma nota (0 a 10): '))

if 9 <= nota <= 10:
    print('Parabéns! Tirou A.')
elif 7 <= nota < 8.9:
    print('Parabéns! Tirou B.')
elif 5 <= nota < 6.9:
    print('Horrível! Tirou C.')
elif 3 <= nota < 4.9:
    print('Péssimo! Tirou D.')
elif 0 <= nota < 2.9:
    print('Um lixo! Tirou E.')
else:
    print('Nota inválida.')