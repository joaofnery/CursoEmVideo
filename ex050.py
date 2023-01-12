resp = 0
for c in range(0,6):
    num = int(input('Escreva um número para ser somado: '))
    if num % 2 == 0:
        resp += num
print('A soma dos números PARES é {}.'.format(resp))