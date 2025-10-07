# Exercício Python 085:
# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

numero = [[],[]]
while True:
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        numero[0].append(n)
    else:
        numero[1].append(n)

    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
          resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

numero[0].sort()
numero[1].sort()
print('='*20)
print(f'os números pares: {numero[0]}')
print(f'os números ímpares: {numero[1]}')