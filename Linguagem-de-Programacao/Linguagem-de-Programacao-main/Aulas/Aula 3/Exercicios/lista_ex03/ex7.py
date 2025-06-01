peso = float(input("Digite o peso do peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está com peso normal.")
elif 25 <= imc < 30:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")
    