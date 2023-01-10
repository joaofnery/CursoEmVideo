##Exercício Python 42:
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

l1 = float(input('Lado 1 do triangulo? '))
l2 = float(input('Lado 2 do triangulo? '))
l3 = float(input('Lado 3 do triangulo? '))

if l1 + l2 > l3 and l1 + l2 > l2 and l2 + l3 > l1:
    if l1 == l2 and l2 == l3:
        print('Triangulo Equilatero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Triangulo Isósceles')
    else:
        print('Triangulo Escaleno')
else:
    print('Essas dimensões não formam um triangulo.')
