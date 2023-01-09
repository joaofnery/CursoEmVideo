##Exercício Python 038:
# Escreva um programa que leia dois números inteiros e
# compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1 = int(input('Escreve um número interiro: '))
num2 = int(input('Escreve outro número inteiro: '))

if num1 == num2:
    print('\033[31mNão existe\033[m valor maior. Os dois são iguais!!')
elif num1 > num2:
    print('\033[31mO primeiro valor\033[m é maior!')
else:
    print('\033[31mO segundo valor\033[m é maior.')
