##Exercício Python 094: 
# Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

from datetime import datetime
mulher = list()
dados = list()

media = 0

while True:
    
    pessoa = dict()
    
    pessoa['nome'] = str(input('Digite seu nome: '))
    pessoa['sexo'] = str(input('Digite o sexo [F/M]: ')).upper().strip()[0]
    nasc = int(input('Digite o ano de seu nascimento: '))
    ano = datetime.now().year
    pessoa['idade'] = ano - nasc

    
    dados.append(pessoa.copy()) 
    
    media += pessoa['idade']
    
    if pessoa['sexo'] == 'F':
        mulher.append(pessoa.copy())
    

    
    opcao = str(input('Deseja Continuar [S/N]: ')).upper().strip()[0]
    
    while opcao not in 'SN':
        opcao = str(input('Opcao inválida! Deseja continuar [S/N]')).upper().strip()[0]
        
    if opcao == 'N':
        break
    
print('-='*30)    

print(f'\n A - Total de pessoas cadastradas: {len(dados)}')

print('-='*30)

print(f'B- A média das idades: {media/len(dados):.2f}')

acimamedia = []
for p in dados:
    if p['idade'] > (media/len(dados)):
        acimamedia.append(p.copy())

print('-='*30)

print(f'C- Quem esta acima da media: {acimamedia}')

print('-='*30)
print(f'{dados}')

print('-='*30)
print(f'\n D - As mulheres são: {mulher}')


print('-----------------FIM----------------')


"""
CODIGO GUANABARA

galera = list()
pessoa = dict()
soma = media = 0

while True:

    pessoa.clear()
    
    pessoa["nome"] = str(input('Digite o nome: '))
    pessoa["idade"] = int(input('Digite sua idade: '))
    

    while True:
        pessoa["sexo"] = str(input('Digite o sexo [M/F]: ')).upper()[0]
        if pessoa["sexo"] in 'MF':
            break
        print('Erro! por favor digite apenas M ou F')

    soma += galera['idade']
    galera.append(pessoa.copy())
    
    while True:
        resp = str(input('Deseja Continuar ! [S/N]: ))    
        if resp not in 'SN':
            break
        print('Erro! por favor digite apenas S ou N')

    if resp == 'S':
        break    

print('-='*30)
print(f'A - Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print('-='*30)
print(f'B - A média de idade é de {media:5.2f} anos.')
print('-='*30)
print(f'C - As mulheres cadastradas foram: ', end=' ')
for p in galera:
    if p['sexo'] == 'F'
        print(f'{p["nome"]} ', end=" ")
print()
print('-='*30)
print('D - Pessoas que estão acima da media: ')
for p in galera:
    if p["idade"] >= media:
       print('     ')
       for k , v in p.items():
            print(f'{k} = {v}; ', end='')
       print() 

print('-='*10,'ENCERRADO','-='*10)
"""