#Exercício Python 56:
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

listanome = []
listaidade = []
listasexo = []
somaidade = 0
idademaisvelho = 0
contmulher = 0
for c in range(1, 5):
    print('----- [{}] PESSOA -----'.format(c))
    nome = str(input('Qual o nome: ')).strip().capitalize()
    listanome.append(nome)
    idade = int(input('Qual a idade de {}: '.format(nome)))
    listaidade.append(idade)
    sexo = str(input('Qual o sexo de {}: '.format(nome))).strip().lower()
    listasexo.append(sexo)
    somaidade += idade
    if sexo == 'masculino' and idade > idademaisvelho:
        idademaisvelho = idade
        maisvelho = nome
    elif sexo == 'feminino' and idade < 20:
        contmulher += 1

media = somaidade / 4

print('A média de idade do grupo é de {} anos.'.format(media))
print('{} é o homem mais velho com {} anos.'.format(maisvelho, idademaisvelho))
print('{} mulheres tem menos de 20 anos.'.format(contmulher))

print(listanome)
print(listaidade)
print(listasexo)