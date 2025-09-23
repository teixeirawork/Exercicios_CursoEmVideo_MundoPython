##Exercício Python 091: 
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter # importa a funcao itemgetter para ordenar o dicionario pelo valor
jogo = dict()
for c in range(1, 5): # para 4 jogadores
    jogo[f'jogador{c}'] = randint(1, 6) # sorteia um numero de 1 a 6 para cada jogador
print('Valores sorteados:') 
for k, v in jogo.items(): # percorre o dicionario jogo
    print(f'O {k} tirou {v} no dado.') # mostra o jogador e o valor do dado
    sleep(1)
print('=-' * 30)
print('  == RANKING DOS JOGADORES ==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # ordena o dicionario pelo valor do dado
for i, v in enumerate(ranking): # percorre a lista ordenada
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('=-' * 30)

