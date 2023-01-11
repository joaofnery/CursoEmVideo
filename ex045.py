##Exercício Python 45:
# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
print('x-'* 30)
print('Vamos Jogar Jokenpo?!')
print('x-'* 30)
mov = str(input('Digite Pedra, Papel ou Tesoura: ')).strip().lower()
lista = ['pedra','papel','tesoura']
movpc = choice(lista)

if mov == movpc:
    print('Você: {} x PC: {}'.format(mov, movpc))
    print('Tente novamente. Foi um EMPATE!')
elif mov == 'pedra' and movpc == 'tesoura':
    print('Você: {} x PC: {}'.format(mov,movpc))
    print('PARABENS! Voce ganhou!')
elif mov == 'pedra' and movpc == 'papel':
    print('Você: {} x PC: {}'.format(mov, movpc))
    print('QUE PENA! Voce perdeu!')
elif mov == 'papel' and movpc == 'pedra':
    print('Você: {} x PC: {}'.format(mov, movpc))
    print('PARABENS! Voce ganhou!')
elif mov == 'papel' and movpc == 'tesoura':
    print('Você: {} x PC: {}'.format(mov, movpc))
    print('QUE PENA! Voce perdeu!')
elif mov == 'tesoura' and movpc == 'pedra':
    print('Você: {} x PC: {}'.format(mov, movpc))
    print('QUE PENA! Voce perdeu!')
elif mov == 'tesoura' and movpc == 'papel':
    print('Você: {} x PC: {}'.format(mov, movpc))
    print('PARABENS! Voce ganhou!')
