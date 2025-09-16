# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


print('-='*10)
temp = []
pessoas = []
gordo = []
magro = []
maior = menor = 0
while True:

    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o Peso: ')))

    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    pessoas.append(temp[:])
    temp.clear()

    opcao = str(input('Deseja continuar S/N: ')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Opção inválida ! deseja continuar S/N: ')).upper().strip()[0]
    if opcao == 'N':
        break

print('-='*30)
print(f'Voce cadastrou: {len(pessoas)} pessoa(s)')
print(f'O Maior peso foi de: {maior} Kg', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print("="*20)
print(f'O Menor peso foi de: {menor} Kg', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print("="*20)

"""
for pessoa in pessoas:
    if len(gordo) == 0 and len(magro) == 0:
        gordo.append(maior)
        magro.append(menor)

    if pessoa[1] >= gordo[-1]:
        gordo.append(pessoa[1])
    if pessoa[1] <= magro[-1]:
        magro.append(pessoa[1])

"""







"""
I.A

# Lista para armazenar pessoas como listas [nome, peso]
grupo = []

while True:
    nome = input("Nome: ")
    peso = float(input("Peso: "))
    grupo.append([nome, peso])

    continua = input("Quer continuar? [S/N] ").strip().upper()
    if continua == 'N':
        break

print(f"Foram cadastradas {len(grupo)} pessoas.")

# Inicializar maior e menor peso com o peso da primeira pessoa
maior_peso = grupo[0][1]
menor_peso = grupo[0][1]

# Encontrar o maior e menor peso
for pessoa in grupo:
    if pessoa[1] > maior_peso:
        maior_peso = pessoa[1]
    if pessoa[1] < menor_peso:
        menor_peso = pessoa[1]

# Criar listas para pessoas mais pesadas e mais leves
mais_pesadas = []
mais_leves = []

# Separar as pessoas conforme o peso
for pessoa in grupo:
    if pessoa[1] == maior_peso:
        mais_pesadas.append(pessoa[0])
    if pessoa[1] == menor_peso:
        mais_leves.append(pessoa[0])

print(f"Pessoas mais pesadas ({maior_peso}kg): {mais_pesadas}")
print(f"Pessoas mais leves ({menor_peso}kg): {mais_leves}") 
"""