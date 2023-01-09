##Exercício Python 040:
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi sua segunda nota? '))
print('x-' * 20)
print('CALCULANDO....')
print('x-' * 20)

media = (nota1 + nota2) / 2

if media < 5:
    print('Sua média foi {:.1f}, você está \033[1;31mREPROVADO!!\033[m'.format(media))
elif media >= 7:
    print('\033[1;32mPARABÉNS!\033[m Sua média foi {:.1f}. Você está \033[32mAPROVADO!\033[m'.format(media))
else:
    print('Você está de \033[1;33mRECUPERAÇÃO!\033[m Média {:.1f}'.format(media))
