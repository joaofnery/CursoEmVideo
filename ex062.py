#Exercício Python 62:
# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
a1 = int(input('Escreva o primeiro termo da PA: '))
r = int(input('Escreva qual a razão da PA: '))
t = 1
c = 10
termo = 1
while termo != 0:
    while t <= c:
        an = a1 + r * (t - 1)
        print('a{}={}'.format(t, an), end=" ")
        t += 1
    termo = int(input('Quantos termos a mais: '))
    c += termo
