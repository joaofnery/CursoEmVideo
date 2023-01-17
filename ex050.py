#Exercício Python 50:
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

resp = 0
for c in range(0, 6):
    num = int(input('Escreva um número para ser somado: '))
    if num % 2 == 0:
        resp += num
print('A soma dos números PARES é {}.'.format(resp))
