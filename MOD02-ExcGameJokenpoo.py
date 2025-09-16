from time import sleep
print ("=========================== MOD 02 EXC GAME JOKENPO =======================")
# CRIE UM PROGRAMA QUE JOGUE JOKENPO COM O USUARIO
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')

print('-=' * 12)
print('0 -  Pedra')
print('1 -  Papel')
print('2 -  Tesoura')
print('-=' * 12)

opcao = int(input('Digite sua Jogada: '))
comp = randint(0,2)
print('-=' * 12)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-=' * 12)

if comp == 0:
    if opcao == 0:
        print('O jogo Empatou jogador escolheu {}\n'.format(itens[opcao]))
        print('o computador escolheu {}'.format(itens[comp]))
    elif opcao == 1:
        print('Voce Ganhou, jogador escolheu {}\n'.format(itens[opcao]))
        print('o computador escolheu {}'.format(itens[comp]))
    elif opcao == 2:
        print('Voce Perdeu, Jogador escolheu {}\n'.format(itens[opcao]))
        print('o computador escolheu {}'.format(itens[comp]))
    else:
        print('jogada inválida o Jogador escolheu {}\n'.format(opcao))
        print('o computador escolheu {}'.format(itens[comp]))
if comp == 1:
    if opcao == 0:
        print('Voce perdeu, o jogador escolheu {}\n'.format(itens[opcao]))
        print('o computador escolheu {}'.format(itens[comp]))
    elif opcao == 1:
        print('Voce Empatou, o jogagor escolheu {}\n'.format(itens[opcao]))
        print('o computador escolheu {}'.format(itens[comp]))
    elif opcao == 2:
        print('Você ganhou, o jogador escolheu {}\n'.format(itens[opcao]))
        print('o computador escolheu {}'.format(itens[comp]))
    else:
        print('Jogada invalida, Jogador escolheu {}\n'.format(itens[opcao]))
        print('o computador escolheu {}'.format(itens[comp]))

if comp == 2:
    if opcao == 0:
        print('Voce ganhou, o jogador escolheu {}\n'.format(itens[opcao]))
        print('o computador escolheu {}'.format(itens[comp]))
    elif opcao == 1:
        print('voce perdeu, o jogador escolheu {}\n'.format(itens[opcao]))
        print('o computador escolheu {}'.format(itens[comp]))
    elif opcao == 2:
        print('voce empatou, o jogador escolheu {}\n'.format(itens[opcao]))
        print('o computador escolheu {}'.format(itens[comp]))
    else:
        print('Jogada inválida, O jogador escolheu {}\n'.format(itens[opcao]))
        print('o computador escolheu {}'.format(itens[comp]))

print ("=========================== MOD 02 EXC GAME JOKENPO =======================")