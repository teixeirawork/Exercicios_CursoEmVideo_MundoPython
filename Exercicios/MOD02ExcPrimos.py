##Exercício Python 52: Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.


print('-='*6,'MOD 02 - EXC NUMEROS PRIMOS','-='*6)

n = int(input('Digite um número para saber se é primo: '))
tot = 0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[33m {}'.format(c),end='')
        tot += 1
    else:
        print('\033[m {}'.format(c),end='')
if tot == 2:
    print('\n \033[mO número: {} é primo \n Foi Divisível {} vezes'.format(n,tot))
else:
    print('\n \033[mO número: {} não é primo \n Foi Divisível {} vezes'.format(n, tot))
print('-='*6,'MOD 02 - EXC NUMEROS PRIMOS','-='*6)