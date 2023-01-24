num = int(input('Digite um número para saber o seu fatorial: '))
c = num
print(num, end="x")
while c != 1:
    c += -1
    num = num * c
    print(c, end="x")
print('=', num)
