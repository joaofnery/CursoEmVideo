#Exercício Python 63:
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela
# os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
n = int(input('Quantos termos vc quer ver da sequencia de Fibonacci? '))
a1 = 0
a2 = 1
t = 3
print(a1)
print(a2)
while t != n:
    a3 = a1 + a2
    print("[a{}] = {}".format(t, a3))
    a1 = a2
    a2 = a3
    t += 1