#Exercício Python 57:
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Qual o sexo da pessoa[M/F]? ')).strip().upper()[0]

while sexo != "M" and sexo != "F":

    sexo = str(input('Você digitou uma forma inválida, colocar [M/F]: ')).strip().upper()
print('Sexo = [{}]'.format(sexo))