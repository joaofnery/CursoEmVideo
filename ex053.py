frase = str(input('Digite uma frase e veja se ela é um palindromo: ')).split()
junto = "".join(frase)

for c in range(0, len(junto) + 1):
    for i in range(len(junto), 0, -1):
        if junto[c] == junto[i]:
            print('Essa frase é um PALINDROMO')
        else:
            print('Não é um palindromo!')