# Exercício 1
texto = input("Digite um texto: ")
palavras = texto.split()
frequencia = {}

for palavra in palavras:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1

print(f'Frequência das palavras: {frequencia}')

# Exercício 2
palavras_unicas = sorted(set(palavras))
print(f'Palavras únicas em ordem crescente:{palavras_unicas}')

# Exercício 3
letras_distintas = sorted(set(letra.lower() for letra in texto if letra.isalpha()))
print(f'Letras distintas ordenadas:{letras_distintas}')