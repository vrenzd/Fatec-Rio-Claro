compra = float(input('Digite o valor da compra: R$'))

if compra > 100:
    print('O frete é grátis')
else:
    frete = 0.15 * compra
    compra = compra + frete
    print(f'O frete ficou em R${compra:.2f}')