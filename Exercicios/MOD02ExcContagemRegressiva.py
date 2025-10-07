print('-='*6,'MOD 02 - EXCERCiCIO CONTAGEM REGRESSIVA','-='*6)
#ESCREVA UM PROGRAMA QUE FAÇA UMA CONTAGEM REGRESSIVA E MOSTRE NA TELA COM O TIME DE 1 SEGUNDO
from time import sleep
for c in range(4,0,-1):
    sleep(0.5)
    print(c)

print('-='*6,'MOD 02 - EXCERCiCIO CONTAGEM REGRESSIVA','-='*6)



print('-='*6,'MOD 02 - EXCERCiCIO CONTAGEM DE PARES','-='*6)

#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range(2,7,2):
    sleep(0.5)
    print(c)
print('-='*6,'MOD 02 - EXCERCiCIO CONTAGEM DE PARES','-='*6)



print('-='*6,'MOD 02 - EXCERCiCIO CONTAGEM DE IMPARES','-='*6)
# FAÇA UM PROGRAMA QUE SOMA TODOS OS NÚMEROS MULTIPLOS DE 3 DE 1 A TE 500

soma = 0
cont = 0

for c in range(1,501,2):
    if c % 3 == 0:
        soma +=  c
        cont +=  1

print ('A soma de todos os valores é :{}'.format(soma))
print('A quantidade de números solicitados são: {}'.format(cont))

print('-='*6,'MOD 02 - EXCERCiCIO CONTAGEM DE IMPARES','-='*6)
