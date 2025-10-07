'''
onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
 mostrando no final quantos palpites foram necessários para vencer.
'''


print('-=*=-'*6,'MOD 03 EXC  - VALIDADOR DE SEXO','-=*=-'*6)

from random import randint

computador = randint(0,10)
print('Sou seu computador, e pensei em um numero entre 0 e 10, Tente Adivinhar...')
jogador = int(input('Digite um numero de 0 a 10: '))
cont = 0

while jogador != computador:
    jogador = int(input('Digite um numero de 0 a 10: '))
    cont +=1

    if jogador == computador:
        cont += 1
        print('Você Venceu, com {} palpites'.format(cont))
    else:

        if jogador < computador:
            print('Chegou perto... Seu Número é menor !')
        else:
            print('Quase lá... Seu Número é maior !')

print('FIM DO JOGO')
print('-=*=-'*6,'MOD 03 EXC  - VALIDADOR DE SEXO','-=*=-'*6)