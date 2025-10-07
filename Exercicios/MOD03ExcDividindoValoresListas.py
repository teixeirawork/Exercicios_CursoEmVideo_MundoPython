# Exercício Python 082:
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

par = []
valores = []
impar = []
while True:

    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    opcao = str(input('Deseja continuar: S/N: ')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Caractere inválido Deseja continuar: S/N: ')).upper().strip()[0]
    if opcao == 'N':
        break
print('-=' * 30)
valores.sort()
print(f'Os valores digitados foram: {valores}')
print('-=' * 30)
par.sort()
print(f'Os valores pares digitados foram: {par}')
print('-=' * 30)
impar.sort()
print(f'Os valores impares digitados foram: {impar}')
