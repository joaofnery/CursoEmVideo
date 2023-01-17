#Exercício Python 53:
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase e veja se ela é um palindromo: ')).strip().split()
junto = "".join(frase)
inverso = ""

for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]

if junto == inverso:
    print('Essa frase é um PALINDROMO')
else:
    print('Não é um palindromo!')