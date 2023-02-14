tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite número entre 0 e 20. '))
while num not in range(0, 21):
    num = int(input('Tente novamente! Digite número entre 0 e 20. '))
print(tupla[num])
