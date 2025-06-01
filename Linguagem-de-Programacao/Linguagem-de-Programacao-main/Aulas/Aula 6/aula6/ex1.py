n1 = float(input("Qual foi a sua nota de trabalho de laboratório? " ))
n2 = float(input("Qual foi a sua nota na avaliação semestral? " )) 
n3 = float(input("Qual foi a sua nota no exame final? "))

media = ((n1*2 + n2*3 + n3*5)/10)

if media >= 8.0:
    print('A')
if 7.0 >= media <= 7.9:
    print("B")
if 6.0 >= media >= 6.9:
    print('C')
if 5.0 >= media <= 5.9:
    print("D")
if media <= 4.9:
    print("E")




