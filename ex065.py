
num = int(input('Digite um número: '))
tnum = num
cont = 1
maior = num
menor = num
c = input('Deseja colocar mais um número? [s/n] ')

while c == "s":

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

