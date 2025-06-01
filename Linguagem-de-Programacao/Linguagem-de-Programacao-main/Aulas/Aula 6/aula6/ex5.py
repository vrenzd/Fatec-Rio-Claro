sal_bruto = float(input("Qual é o seu salário bruto?"))

if sal_bruto <= 2112:
    print("Você é isento, não precisa pagar!")
if sal_bruto >= 2112.01 and sal_bruto <=2826.65:
    aliquota = 0.075
    par_deduzir = 158.40
    imposto_renda = (sal_bruto * aliquota) - par_deduzir
    print(f"O imposto de renda a ser pago é de R${imposto_renda:.2f}")

if sal_bruto >= 2826.66 and sal_bruto <= 3751.05:
    aliquota = 0.15
    par_deduzir = 370.40
    imposto_renda = (sal_bruto * aliquota) - par_deduzir
    print(f"O imposto de renda a ser pago é de R${imposto_renda:.2f}")

if sal_bruto >= 3751.06 and sal_bruto <=4664.68:
    aliquota = 0.225
    par_deduzir = 651.73
    imposto_renda = (sal_bruto * aliquota) - par_deduzir
    print(f"O imposto de renda a ser pago é de R${imposto_renda:.2f}")

if sal_bruto > 4664.68:
    aliquota = 0.275
    par_deduzir = 884.96
    imposto_renda = (sal_bruto * aliquota) - par_deduzir
    print(f"O imposto de renda a ser pago é de R${imposto_renda:.2f}")
