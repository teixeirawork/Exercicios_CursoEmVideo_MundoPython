##Exercício Python 098:
# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 
# b) de 10 até 0, de 2 em 
# c) uma contagem personalizada

from time import sleep

# Faça um programa que tenha uma função chamada contador()
def contador(inicio,fim,passo):
    
    
    # a) de 1 até 10, de 1 em
    print('de 1 até 10, de 1 em 1') 
    sleep(2)
    for c in range (1, 11,1):
        print(f'{c}',end='-',flush=True)
        sleep(0.5)
    print()
     
    # b) de 10 até 0, de 2 em
    print('de 10 até 0, de 2 em 2')
    sleep(2)
    for c in range(10 , -1 , -2):
        print(f'{c}',end='-',flush=True)
        sleep(0.5) 
    print() 
    
     # c) uma contagem personalizada
    print(f'Contagem de {inicio} até o {fim} de {passo} em {passo}', end='' )
    sleep(2)
    print()

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    
    for c in range (inicio,fim+1,passo):
        print(f'{c}',end='-', flush=True)
        sleep(0.5)
    print()    
    
    
    
    if inicio > fim:
        for c in range (inicio,fim-1,-passo):
            print(f'{c}',end='-',flush=True)
            sleep(0.5)
        print()
    
    
ini = int(input('Inicio da contagem: '))
fim = int(input('Fim da contagem: '))
passo = int(input('Passo da contagem: '))

contador(ini, fim, passo)



"""
RESPOSTA DO GUANABARA

from time import sleep

def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    
    print('-='*20)
    print(f'Contage de {i} ate {f} de {p} em {p}') 
    sleep(1)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end='', flush=True)    
            sleep(0.5)
            cont -= p
        print(FIM!)


#programa principal
contador(1,10,1)
contador(10,0,2)
print('-='*20)
print('Agora e sua vez de personalizar a contagem: ')
ini = int(input('Incio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))

contador(ini,fim,pas)
"""