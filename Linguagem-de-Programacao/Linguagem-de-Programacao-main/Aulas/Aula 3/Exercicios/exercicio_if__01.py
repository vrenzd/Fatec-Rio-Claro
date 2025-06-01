idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salário: R$'))
beneficio = 0

if beneficio > 18 and beneficio <= 2000:
    print('Tem direito ao benefício')
elif beneficio > 60:
    print('Tem direito ao benefício')
else:
    print('Não tem direito ao benefício')