print('='* 30)
titulo = 'BANCO KELB'
print(titulo.center(30, " "))
print('='* 30)
valorstr = " "
while valorstr.isdigit() == False:
    valorstr = input('Qual valor você quer sacar: R$')
valor = int(valorstr)
ced50 = valor // 50
valor = valor - ced50 * 50
ced20 = valor // 20
valor = valor - ced20 * 20
ced10 = valor // 10
valor = valor - ced10 * 10
ced1 = valor // 1

print(f'{ced50} cédulas de R$50.')
print(f'{ced20} cédulas de R$20.')
print(f'{ced10} cédulas de R$10.')
print(f'{ced1} cédulas de R$1.')
