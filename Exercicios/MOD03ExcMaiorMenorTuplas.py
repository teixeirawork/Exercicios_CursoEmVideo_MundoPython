## Exercício Python 074:
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

print('='*6,'MOD 03 - EXC MAIOR E MENOR EM TUPLAS','='*6)

from random import randint

num = (randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))
print(f'os números sorteados foram: ',end='')
for c in num:
    print(f'{c}',end=' ')
print(f'\nO maior numero sorteado foi: {max(num)}')
print(f'O menor numero sorteado foi: {min(num)}')


'''
    FIZ  UMA GAMBIARRA APARECEU O RESULTADO CORRETO, MAS O SCRIPT ESTÁ ERRADO

for i in range(0,5):
    var = randint(1,100)
    print(f'-> {var}', end=' ')
    if i == 0:
        maior = var
        menor = var
    else:
        if var > maior:
            maior = var
        if var < menor:
            menor = var
print(f'\n O maior numero foi: {maior}')
print(f'O menor numero foi: {menor}')
'''





print('\n','='*6,'MOD 03 - EXC MAIOR E MENOR EM TUPLAS','='*6)