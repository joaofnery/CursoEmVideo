#Exercício Python 61:
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
a1 = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão dessa PA? '))
a = 1
while a <= 10:

    ai = a1 + r * (a - 1)
    print('a{}={}'.format(a, ai), end=" ")
    a += 1
