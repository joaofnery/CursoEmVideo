from random import randint
print('-='* 20)
print('Vamos jogar PAR ou IMPAR!')
print('-='* 20)
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    jogada = input('PAR ou IMPAR? [P/I]').strip().upper()[0]
    pc = randint(0, 10)
    resultado = jogador + pc

    if resultado%2 == 0 and jogada == 'I':
        print(f'Você jogou {jogador} e o PC {pc}. Total {resultado} DEU PAR')
        print('Você PERDEU!')
        break
    elif resultado%2 != 0 and jogada == "P":
        print(f'Você jogou {jogador} e o PC {pc}. Total {resultado} DEU IMPAR')
        print('Você PERDEU!')
        break
    elif resultado%2 == 0 and jogada == "P":
        print(f'Você jogou {jogador} e o PC {pc}. Total {resultado} DEU PAR')
        print('Você VENCEU!!')
        vitoria += 1
    elif resultado%2 != 0 and jogada == "I":
        print(f'Você jogou {jogador} e o PC {pc}. Total {resultado} DEU IMPAR')
        print('Você VENCEU!!')
        vitoria += 1
print(f'GAME OVER! Você venceu {vitoria} vezes.')
