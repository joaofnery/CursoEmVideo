numero = int(input('Escreva um número para ser convertido: '))
base = int(input('Digite 1 para Binário,\n2 para Octal, \n3 para hexadecimal. '))

if base == 1:
    convert = format(numero, "b")
    print(convert)
elif base == 2:
    convert = format(numero, "o")
    print(convert)
elif base == 3:
    convert = format(numero, "x")
    print(convert)
else:
    print('Você deve escolher a conversão entre 1,2 e 3.')
