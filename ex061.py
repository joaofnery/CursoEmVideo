a1 = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão dessa PA? '))
a = 1
while a != 11:

    ai = a1 + r * (a - 1)
    print('a{}={}'.format(a, ai), end=" ")
    a += 1
