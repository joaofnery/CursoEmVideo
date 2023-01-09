##Exercício Python 041:
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

import datetime
anonascimento = int(input('Qual ano de nascimento? '))
anoatual = datetime.date.today()

idade = anoatual.year - anonascimento

if idade < 9:
    print('categoria MIRIM. {} ANOS'.format(idade))
elif idade >= 9 and idade < 14:
    print('Categoria INFANTIL. {} ANOS'.format(idade))
elif idade >=14 and idade < 19:
    print('categoria JUNIOR. {} ANOS'.format(idade))
elif idade >= 19 and idade < 20:
    print('categoria SENIOR. {} ANOS.'.format(idade))
elif idade >= 20:
    print('categoria MASTER! {} ANOS'.format(idade))
