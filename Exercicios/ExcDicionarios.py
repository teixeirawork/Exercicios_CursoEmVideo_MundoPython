# AULA INCIAL DE DICIONARIOS PYTHON
#Observação: Dicionarios sao mutaveis, ou seja, podem ser alterados apos a criacao
    # chaves: sao unicas e imutaveis, ou seja, nao podem ser alteradas = dicionario.keys()
    # valores: podem ser de qualquer tipo de dado, inclusive outros dicionarios = dicionario.values()
    # items: sao ordenados a partir do Python 3.7, ou seja, mantem a ordem de insercao = dicionario.items()


# Dicionarios sao estruturas de dados que armazenam pares de chave e valor

# Exemplo de dicionario
pessoa = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}
print(pessoa)

# Acessando valores do dicionario
print(pessoa['nome'])
print('----------------------------------')
print(pessoa['idade'])
print('----------------------------------')
print(pessoa['cidade'])

# Adicionando novos pares chave-valor
pessoa['profissão'] = 'Engenheiro'
print('----------------------------------')
print(pessoa)
print('-------------CHAVE KEY---------------------')
print(pessoa.keys())
print('------------VALORES VALUE()----------------------')
print(pessoa.values())
print('-------------ITEMS ITENS()---------------------')
print(pessoa.items())   
print('----------------------------------')

# Modificando valores existentes
pessoa['idade'] = 26
print(pessoa)

# Removendo pares chave-valor
del pessoa['cidade']
print(pessoa)
print('------------UTILIZANDO FOR----------------------')
# Iterando sobre um dicionario
for chave, valor in pessoa.items(): # desempacotamento de dicionarios com for utilizando items() - no caso de values() so pega os valores ou keys() so pega as chaves
    print(f'{chave}: {valor}')
# Verificando se uma chave existe
print('-------------UTILIZANDO IF---------------------') 
if 'nome' in pessoa:
    print('A chave "nome" existe no dicionario.')
else:
    print('A chave "nome" não existe no dicionario.')

# Obtendo todas as chaves
chaves = pessoa.keys()
print(chaves)

# Obtendo todos os valores
valores = pessoa.values()
print(valores)

# Obtendo todos os itens (pares chave-valor)
itens = pessoa.items()
print(itens)

# Limpando o dicionario
pessoa.clear()
print(pessoa)

# lista de dicionarios
print('-------------LISTA DE DICIONARIOS---------------------')
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]) # acessando o primeiro dicionario da lista
print(brasil[1]) # acessando o segundo dicionario da lista
print(brasil[0]['uf']) # acessando o valor da chave 'uf' do primeiro dicionario da lista
print(brasil[1]['sigla']) # acessando o valor da chave 'sigla' do segundo dicionario da lista
print('----------------------------------')
# Iterando sobre a lista de dicionarios
for estado in brasil:
    for chave, valor in estado.items():
        print(f'O campo {chave} tem valor {valor}.')
    print('----------------------------------')
print('----------------------------------')
# Copiando dicionarios
estado = dict(uf='Minas Gerais', sigla='MG') # outra forma de criar dicionarios
print(estado)
print('----------------------------------')
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
estado3 = estado1.copy() # copiando o dicionario estado1 para estado3
brasil.append(estado3)
print(brasil)
print('----------------------------------')
# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
valorproduto = float(input('Digite o valor do produto R$: '))
valordesconto = valorproduto * 5/100
valorfinal = valorproduto - valordesconto
print('o valor do desconto R$: {}\n valor final do produto R$: {} '.format(valordesconto, valorfinal))
print('----------------------------------')
    