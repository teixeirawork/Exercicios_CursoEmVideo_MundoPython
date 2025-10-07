# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.


print('---------- MOD 03 - EXC AVALIADOR DE PRODUTOS--------------')
prodbarato = ''
vlrbarato = total = maisdemil = 0

while True:
    prod = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: '))
    deslig = str(input('Deseja Cadastrar outro Produto: [S/N]: ')).upper().strip()[0]
    total += preco
    if vlrbarato == 0 and prodbarato == '':
        prodbarato = prod
        vlrbarato = preco

    if preco < vlrbarato:
        vlrbarato = preco
        prodbarato = prod

    if preco > 1000:
        maisdemil += 1

    while deslig not in 'NS':
        deslig = str(input('Deseja Cadastrar outro Produto: [S/N]: ')).upper().strip()[0]
    if deslig == 'N':
        break
print(f'O valor Total dos produtos foi: {total:.2f}')
print(f'O produto mais barato foi: {prodbarato} que custa R$: {vlrbarato:.2f}')
print(f'A quantidade de produtos com valor maior que R$1000 foi: {maisdemil}')