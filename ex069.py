pessoas18 = homens = mulheres20 = 0
while True:
    print('x-'* 20)
    print('CADASTRE UMA PESSOA')
    print('x-'* 20)
    idade = ""
    sexo = ""
    cont = ""

    while idade.isdigit() == False:
        idade = input('Idade: ')
    idadeint = int(idade)
    while sexo != "M" and sexo != "F":
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    if idadeint > 18:
        pessoas18 += 1
    if sexo == "M":
        homens += 1
    if idadeint < 20 and sexo == "F":
        mulheres20 += 1
    print('x-'* 20)
    while cont not in ["S","N"]:
        cont = input('Quer continuar? [S/N]').strip().upper()[0]
    if cont == "N":
        break
print('FIM DO PROGRAMA')
print(f'Total de pessoas com mais de 18 anos: {pessoas18}')
print(f'Ao todo temos {homens} Homens cadastrados.')
print(f'E temos {mulheres20} mulheres com menos de 20 anos.')