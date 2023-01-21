opc = 0
while opc != 5:
    num1 = float(input('Digite o [1] número: '))
    num2 = float(input('Digite o [2] número: '))

    print('O que você gostaria de fazer com esses números?')
    opc = int(input(''' 
                        Digite [1] para Somar
                        Digite [2] para Multiplicar
                        Digite [3] para Saber qual maior valor
                        Digite [4] para Novos números
                        Digite [5] para Sair do programa'''))
    if opc == 1:
        total = num1 + num2
        print('{} + {} = {} (SOMA)'.format(num1, num2, total))
    elif opc == 2:
        total = num1 * num2
        print('{} x {} = {} (MULTIPLICAR)'.format(num1, num2, total))
    elif opc == 3:
        if num1 > num2:
            print('{} é MAIOR que {}'.format(num1, num2))
        else:
            print('{} é MAIOR que {}'.format(num2, num1))
    elif opc == 4:
        print('OK')
print('FIM')