from random import randint
pc = pc = randint(0, 10)
vc = int(input('Diga um número entre 0 e 10, e veja se foi o mesmo que o PC: '))
palpite = 1
if pc == vc:
    print('Parabéns! Você acertou com [{}] palpite!'.format(palpite))
else:
    while vc != pc:
        palpite += 1
        vc = int(input('Você errou. Tente novamente: '))
print('Parabéns!! Você acertou com [{}] palpites!'.format(palpite))
