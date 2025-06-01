dia = int(input("Digite o dia:"))
mes = int(input("Digite o número do mês:"))
ano = int(input("Digite o ano:"))

if mes == 1:
    mes = "janeiro"
if mes == 2:
    mes = "fevereiro"
if mes == 3:
    mes = "março"
if mes == 4:
    mes = "abril"
if mes == 5:
    mes = "maio"
if mes == 6:
    mes = "junho"
if mes == 7:
    mes = "julho"
if mes == 8:
    mes = "agosto"
if mes == 9:
    mes = "setembro"
if mes == 10:
    mes = "outubro"
if mes == 11:
    mes = "novembro"
if mes == 10:
    mes = "dezembro"

print(f'{dia}/{mes}/{ano}')

