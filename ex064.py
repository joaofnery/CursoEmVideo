total = 0
c = 0
num = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        c += 1
        total += num
print('Voce digitou {} números e o total foi {}.'.format(c, total))
