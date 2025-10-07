##Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


print('-=|*|=-'*10,'MOD 03 - EXC CAIXA ELETRÔNICO','-=|*|=-'*9)
ced = 50
vlrsaq = int(input('Digite o valor que deseja sacar R$: '))
totced = 0

while True:
    if vlrsaq >= ced:
        vlrsaq -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'Total de Cedulas: {totced}, cedulas de R$: {ced}')
        if ced == 50:
           ced = 20
        elif ced == 20:
           ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if vlrsaq == 0:
             break

print('-=|*|=-'*10,'MOD 03 - EXC CAIXA ELETRÔNICO','-=|*|=-'*9)