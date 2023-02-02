while True:
    num = int(input('Digite o número para ver a sua tabuada: '))
    if num < 0:
        break
    n = 0
    while n != 11:
        total = n * num
        print(f'{n} x {num} = {total}')
        n += 1
