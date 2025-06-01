idade_atleta = int(input('Digite a idade: '))

if idade_atleta <= 12:
    print('Infantil')
elif 13 <= idade_atleta < 17:
    print('Juvenil')
elif 18 <= idade_atleta < 40:
    print('Adulto')
else:
    print('Veterano')
    