
maiorpeso = 0.0
menorpeso = 1000.0
for c in range(1, 6):
    pesoi = float(input('Digite o peso [{}] para ser comparado: '.format(c)))
    if pesoi > maiorpeso:
        maiorpeso = pesoi
    elif pesoi < menorpeso:
        menorpeso = pesoi

print('O maior peso lido foi {}kg e o menor {}kg.'.format(maiorpeso, menorpeso))
