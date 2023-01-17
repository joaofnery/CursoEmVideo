from datetime import date
contadormaior = 0
contadormenor = 0
for c in range(0, 7):
    nascimento = int(input('Qual ano de nascimento? '))
    anoatual = date.today().year
    if anoatual - nascimento >= 21:
        contadormaior += 1
    elif anoatual - nascimento < 21:
        contadormenor += 1

print('''   {} pessoas atingiram a maior idade
            {} pessoas ainda não atingiram a maior idade'''.format(contadormaior, contadormenor))
