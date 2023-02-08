#Exercício Python 58:
# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
pc = randint(0, 10)
vc = int(input('Diga um número entre 0 e 10, e veja se foi o mesmo que o PC: '))
palpite = 1
if pc == vc:
    print('Parabéns! Você acertou com [{}] palpite!'.format(palpite))
else:
    while vc != pc:
        palpite += 1
        if vc > pc:
            print('Menos....')
        else:
            print('Mais....')
        vc = int(input('Você errou. Tente novamente: '))
print('Parabéns!! Você acertou com [{}] palpites!'.format(palpite))
