##Exercício Python 092:
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime
ano = datetime.date.today().year
trabalhador = list()
while True:
    
    cadworker = dict()
    
    nome  = str(input('Digite seu nome: '))
    nasc = int(input('Digite em qual ano você nasceu: '))
    cpts = int(input('Digte o ano da sua Carteira de Trabalho: '))
    idade  = ano - nasc
    timeworker = ano - cpts
    
    
    cadworker['nome'] = nome
    cadworker['idade'] = idade
    cadworker['tempocpts'] = timeworker
    
    if timeworker > 0:
        contrato = int(input('Digite o ano que foi contratado: '))
        salario = float(input('Digite o valor do salário: '))
        cadworker['contrato'] = contrato
        cadworker['salario'] = salario
    
    if 0 < timeworker <= 75:
        aposentadoria = ano - cadworker['contrato']
        tempaposentado = 75 - aposentadoria
        cadworker['Aposentadoria'] = tempaposentado
    else:
        cadworker['Aposentadoria'] = 'Aposentado'
    
    trabalhador.append(cadworker.copy())
    
    
    opcao = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Opção Inválida! Deseja Continuar [S/N] '))
        
    
    if opcao == 'N':
        break
    

print()    
print('-='*10,'Cadastro do trabalhador','-='*10)
for t, i in enumerate(trabalhador):
    print (f'O trabalhador {t} tem as {i}', end=' ')
    print()

