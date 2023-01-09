##Exercício Python 39:
# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# e é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
anonascimento = int(input('Em que ano voce nasceu? '))

anoatual = datetime.date.today()

if anoatual.year - anonascimento < 18:
    dif = 18 - (anoatual.year - anonascimento)
    print('Faltam {} anos para voce se alistar.'.format(dif))
elif anoatual.year - anonascimento > 18:
    dif = (18 - (anoatual.year - anonascimento)) * -1
    print('Já deveria ter se alistado. Se passaram {} anos.'.format(dif))
else:
    print('Este é o ano em que você deve se alistar! \033[32mPARABENS!!\033[m')
