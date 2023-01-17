#Exercício Python 49:
# Refaça o DESAFIO 9, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Qual número você deseja saber a tabuada? '))
for c in range(0, 11):
    resp = num * c
    print(resp)
