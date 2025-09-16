# Exercício Python 079:
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('valor adicionado com sucesso!')
    else:
        print('valor duplicado não adicionado')
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while opcao not in 'SN':
          opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'S':
          continue
    if opcao == 'N':
           break
print('-='*6)
valores.sort()
print(f'voce digitou os valores {valores}')
