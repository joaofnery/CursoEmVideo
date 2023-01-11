##Exercício Python 44:
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

preco = float(input('Informe o preço do produto: '))
forma = int(input('Qual será a forma de pagamento? Digite 1 - a vista Dinheiro/ 2 - a vista cartão/ 3 - 2x no cartão/ 4 - 3x ou mais: '))

if forma == 1:
    precof = preco * 0.9
    print('Pagameno a vista no dinheiro fica R${:.2f}.'.format(precof))
elif forma == 2:
    precof = preco * 0.95
    print('Pagamento a vista no cartão fica R${:.2f}.'.format(precof))
elif forma == 3:
    print('Pagamento em 2x no cartão fica R${:.2f}.'.format(preco))
elif forma == 4:
    precof = preco * 1.2
    print('Pagamento em 3x ou mais, fica R${:.2f}.'.format(precof))
