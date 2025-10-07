# Exercício Python 099: 
# Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* num):
    
    if len(num) == 0:
        print('Nenhum Valor foi informado')
        return
    
    maior_valor = num[0]
    
    for valor in num:
        if valor > maior_valor:
            maior_valor = valor
    
    print(f'O maior valor informado foi {max(maior_valor)}')    

numeros = list()
while True:
    
    
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999: 
        break
    else:
        numeros.append(n)
    
    
print(f'Foram informados {len(numeros)} numeros')    
print('-'*20)
maior(numeros)