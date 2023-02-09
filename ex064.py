# Exercício Python 64:
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
total = c = num = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        c += 1
        total += num
print('Voce digitou {} números e o total foi {}.'.format(c, total))
