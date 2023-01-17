frase = str(input('Digite uma frase e veja se ela é um palindromo: ')).split()
junto = "".join(frase)

for c in range(0, len(junto)):

    if junto[c] == junto[len(junto) - 1 - c]:
        print('Essa frase é um PALINDROMO')
    else:
        print('Não é um palindromo!')