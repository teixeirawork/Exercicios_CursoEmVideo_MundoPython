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
    
    
    
    cadworker['nome'] = nome
    cadworker['idade'] = idade
    cadworker['tempocpts'] = ano - cpts
    
    
    
    if  0 < cadworker['tempocpts'] < 35:
        
        contrato = int(input('Digite o ano que foi contratado: '))
        salario = float(input('Digite o valor do salário: '))
        cadworker['contrato'] = contrato
        cadworker['salario'] = salario
        
        tempocpts = ano - contrato
        aposentadoria = 35 - tempocpts
        idade_aposentar = idade + aposentadoria
         
        cadworker['tempo_aposentar'] = aposentadoria
        cadworker['idade_aposentar'] = idade_aposentar
    
    elif cadworker['tempocpts'] == ano:
        cadworker['Aposentadoria'] = 'Sem Carteira'    
    
    
    else:
        cadworker['Aposentadoria'] = 'Aposentado'
    
    trabalhador.append(cadworker.copy())
    
    
    opcao = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Opção Inválida! Deseja Continuar [S/N] '))
        
    
    if opcao == 'N':
        break
   
   # PARA MOSTRAR UMA LISTA ORDENADA COM DICIONARIOS, PRECISA-SE MONTAR UM DICIONARIO AUXILIAR NO PRIMEIRO FOR
   # EM SEGUIDA PERCORRER ESSE DICIONÁRIO AUXLIAR PARA EXIBIR EM FORMATO DE LISTA {INDEX = VALOR} 
   
print('-='*10,'Cadastro do trabalhador','-='*10)
for idx, t in enumerate(trabalhador,1): # neste for define-se  t como um novo dicionario
    print(f'trabalhador {idx}: ')
    for chave, valor in t.items():  # este for percorre o novo dicionaro t
        print(f' {chave}: {valor}')
    print('----')
    
    
    """
    codigo criado pelo guanabara para resolução do exercicio
    
    from datetime import datetime
    dados = dict()
    dados['nome'] = str(input('Nome: '))
    nasc = int(input('Ano de Nascimento: '))
    dados['idade'] = datetime.now().year - nasc
    dados['cpts'] = int(input('Carteira de Trabalho 0 não tem: '))
    if dados['cpts'] != 0:
        dados['contratacao'] = int(input('Ano de contratação: '))
        dados['salario'] = float(input('Salario R$: '))
        dados ['Aposentadoria'] = dados['idade'] + ((dados[contratacao] +35)- datetime.now().year)
    print('-='*30)
    for k , v in dados.items():
        print(f'{k} tem o valor {v}')
    
    
    
    """