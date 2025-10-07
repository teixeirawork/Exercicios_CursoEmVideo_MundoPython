##Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (desconsiderando o flag).


print('-=|*|=-' * 6, 'MOD 03 - EXC SOMANDO NÚMEROS MENOS FLAG','-=*=-'*6)

flag = 999
n = int(input('Digite um numero [999 para parar]: '))
total = n
cont = 0

while flag != n:

    n = int(input('Digite um numero [999 para parar]: '))
    total += n
    cont += 1
    if n  == 999:
        total -= n

print('A quantidade de números que você digitou foi: {} '.format(cont))
print('a soma dos números digitados foram {}'.format(total))
print('-=|*|=-' * 6, 'MOD 03 - EXC SOMANDO NÚMEROS MENOS O FLAG','-=*=-'*6)