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
        lista.append(randint(1,10))
        print(f'{c}', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')    


def SomaPar(lista):
    for n in lista:
        if n % 2 == 0:
            lista.append(n)
        
     
    
sorteados = list()


print('-'*20,'NUMEROS SORTEADOS','-'*20)
sorteia(sorteados)
print(sorteados)
print('-'*60)

print('-'*20,'NUMEROS PARES','-'*20)
SomaPar(sorteia(sorteados))
print(sorteados)
print('-'*60)