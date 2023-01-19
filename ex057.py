sexo = str(input('Qual o sexo da pessoa[M/F]? ')).strip().upper()

while sexo != "M" and sexo != "F":

    sexo = str(input('Você digitou uma forma inválida, colocar [M/F]: ')).strip().upper()
print('Sexo = [{}]'.format(sexo))