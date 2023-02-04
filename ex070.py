print("=-" * 20)
titulo = "LOJA DO KELBINHO"
print(titulo.center(20, "="))
print("=-" * 20)
total = prod1000 = 0
prodbarato = ""
while True:
    produto = input('Nome do produto: ').strip()
    precostr = ""
    while precostr.isdigit() == False:
        precostr = input('Preço: R$ ')
    preco = int(precostr)
    if total == 0:
        prodbarato = produto
        precobarato = preco
    elif preco < precobarato:
        prodbarato = produto
        precobarato = preco
    if preco > 1000:
        prod1000 += 1

    total += preco
    cont = ""
    while cont not in ["S", "N"]:
        cont = input('Quer continuar: [S/N] ').strip().upper()[0]
    if cont == "N":
            break

fim = "FIM DA COMPRA"
print(fim.center(30, "*"))
print(f'O total foi de R$ {total:.2f}.')
print(f'Temos {prod1000} produtos custando mais de R$ 1000,00.')
print(f'O produto mais barato foi {prodbarato} custando R$ {precobarato:.2f}.')
