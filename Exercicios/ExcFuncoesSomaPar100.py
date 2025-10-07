##Exercício Python 100: 
# Faça um programa que tenha uma lista chamada números e duas funções chamadas 
# sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando valores da Lista: ', end='')
    print()
    for c in range (0,5):
        c = randint(1,10)
        lista.append(c)
        print(f'{c}', end=' ', flush=True)
        sleep(0.3)
    print()
    print('PRONTO!')    


def SomaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista} o total é: {soma}')
     
    
sorteados = list()


print('-'*20,'NUMEROS SORTEADOS','-'*20)
sorteia(sorteados)

print('-'*60)

print('-'*20,'NUMEROS PARES','-'*20)
SomaPar(sorteados)

print('-'*60)