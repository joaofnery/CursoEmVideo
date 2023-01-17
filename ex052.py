#Exercício Python 52:
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Escreva um número e veja se ele é PRIMO: '))
div = 0
for c in range(1, num+1):
    if num % c == 0:
        div += 1
if div == 2:
    print('{} é PRIMO.'.format(num))
else:
    print('{} tem {} divisores, portanto não é primo.'.format(num, div))
