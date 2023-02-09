# Exercício Python 65:
# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
num = int(input('Digite um número: '))
tnum = num
cont = 1
maior = num
menor = num
c = input('Deseja colocar mais um número? [s/n] ')

while c in "s":

    num = int(input('Digite um número: '))
    tnum += num
    cont += 1
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    c = input('Deseja colocar mais um número? [s/n] ')

media = tnum / cont
print('Você digitou {} números e a média deles é {}.'.format(cont, media))
print('Maior valor = {} / Menor valor = {}'.format(maior, menor))
