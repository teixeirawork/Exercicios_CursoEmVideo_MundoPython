##Exercício Python 102: 
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e 
# outro chamado show, que será um valor lógico (opcional) 
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def factorial(primeiro, show = False):
    """
    ->Calcula Factorial de um numero
    :parm primeiro: recebe o numero que vai ser fatoriado
    :parm show: (opcional) exibe ou não o calculo
    
    """
    from math import factorial
    f = factorial(primeiro)
    print(f'O factorial de {primeiro} é: {f}', end='')
    print()
    if show == True:
        while f > 0:
            print(f'-> {f}',end=' ')
            f -= 1

    
 # programa principal
 
# n = int(input('Digite o numero para calcular factorial: '))
# factorial(n,True)

help(factorial)