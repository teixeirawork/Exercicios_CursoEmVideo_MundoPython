## Exercício Python 090: 
# Faça um programa que leia nome e média de um aluno, 
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

# criando um dicionário
turma = list()
while True:
    pessoa = dict()
    nome = str(input('Digite o nome: '))
    media = float(input(f'Digite a média de {nome}: '))
    
    pessoa['nome'] = nome
    pessoa['media'] = media
    
    if media >= 7:
        pessoa['situação'] = 'Aprovado'
    elif 5 <= media < 7:
        pessoa['situação'] = 'Recuperação'
    else:
        pessoa['situação'] = 'Reprovado'        
    
    turma.append(pessoa.copy())
    
    opcao = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Opção inválida! Deseja Continuar? [S/N] ')).upper().strip()[0]
    if opcao in 'N':
        break

print('=-' * 30)
for pessoa in turma:
    for k, v in pessoa.items():
        print(f' - {k} é igual a {v}')
    print('=-' * 3)    
print('=-' * 30)