#Exercício Python 51:
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Escreva o primeiro termo de uma PA: '))
r = int(input('Escreva a razão da PA: '))
print(a1)
for c in range(1, 10):
    a1 += r
    print(a1, end= " ")
