tnum = 0
cont = 0

c = "s"
while c == "s":
    num = int(input('Digite um número: '))
    tnum += num
    cont += 1
    
    c = input('Deseja colocar mais um número? [s/n] ')
    if c != "s":
        media = tnum / cont
        print('Você digitou {} números e a média deles é {}.'.format(cont, media))

