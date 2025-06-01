preco_original = float(input('Digite o preço do produto: R$'))
desconto = 0.10
preco_desconto = preco_original * (1 - desconto)

print(f'O preço do produto com desconto é R${preco_desconto:.2f}.')
