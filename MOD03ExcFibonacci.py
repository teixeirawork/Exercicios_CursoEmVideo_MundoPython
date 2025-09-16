##Exercício Python 63:
# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
print('-=|*|=-' * 6, 'MOD 03 - EXC SEQUÊNCIA DE FIBONACCI','-=*=-'*6)

termos = int(input('Digite a quantidade de termos que deseja mostrar: '))
t1 = 0
t2 = 1
print('-=|*|=-' * 5)
print('{} -> {}'.format(t1,t2), end ='')
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM ')
print('-=|*|=-' * 5,'\n')
print('-=|*|=-' * 6, 'MOD 03 - EXC SEQUÊNCIA DE FIBONACCI','-=*=-'*6)