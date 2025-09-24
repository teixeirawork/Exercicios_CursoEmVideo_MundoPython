# Exercício Python 093:
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

from datetime import datetime
dados = dict()
ano = datetime.now().year
dados['nome'] = str(input('Digite o nome do jogador: '))
dados['partidas'] = int(input('Digite quantas partidas jogou: '))   

goljogo = 0
campeonato = list()
for p in range (1, dados['partidas']+1):
    gols = int(input(f'Quantos gols o jogador fez na {p}º partida '))
    campeonato.append(gols)
    goljogo += gols
    
dados['golspro'] = campeonato
mediagol = goljogo / dados['partidas']
dados['totalgols'] = goljogo

print('-='*10,'PRIMEIRA AMOSTRA','-='*10)

print(dados)

print('-='*10,'PRIMEIRA AMOSTRA','-='*10)

print()

print('-='*10,'SEGUNDA AMOSTRA','-='*10)

for indice, valor in dados.items():
    print(f' O campo {indice} tem valor {valor}')
print()   

print('-='*10,'SEGUNDA AMOSTRA','-='*10)
print()

print('-='*10,'TERCEIRA  AMOSTRA','-='*10)
print(f'O jogador: {dados['nome']} jogou {dados["partidas"]}: ')

for i, g in enumerate(campeonato):
    print(f' => Na partida {i+1}º o jogador fez: {g} gols', end=' ')
    print()
print(f'Foi um total de {dados["totalgols"]}')
print('-='*10,'TERCEIRA  AMOSTRA','-='*10)