idade = int(input('Digite a idade: '))
condicao = input('Gestante, Deficiente ou Normal (G, D): ').upper().strip()

if idade >= 60 or condicao == 'D':
    print('Prioridade máxima.')
elif condicao == 'G':
    print('Gestantes.')
else:
    print('Atendimento normal.')
    