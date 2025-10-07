# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from time import sleep

print('='*30,'SORTEIO MEGA SENA','='*30)
from random import randint

qtjogos = int(input('Digite quantos jogos deseja sortear: '))
lista = []
jogos = []
tot = 0
while tot <= (qtjogos -1):
    cont = 0
    while True:
        num = (randint(1,60))
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('='*3,f'SORTEANDO [{qtjogos}] JOGOS DA MEGA SENA','='*3)
for i, l in enumerate(jogos):
    print(f'Jogo{i+1}: {l}')
    sleep(1)


print('='*30,'BOA SORTE !','='*30)