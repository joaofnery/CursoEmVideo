#Exercício Python 55:
# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maiorpeso = 0.0
menorpeso = 1000.0
for c in range(1, 6):
    pesoi = float(input('Digite o peso [{}] para ser comparado: '.format(c)))
    if pesoi > maiorpeso:
        maiorpeso = pesoi
    elif pesoi < menorpeso:
        menorpeso = pesoi

print('O maior peso lido foi {}kg e o menor {}kg.'.format(maiorpeso, menorpeso))
