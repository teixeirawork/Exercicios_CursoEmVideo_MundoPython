##Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('-=|*|=-' * 6, 'MOD 03 - EXC JOGO DO PAR OU IMPAR COM BREAK ','-=*=-'*6)

cont = 0
while True:
    comp = randint(1, 10)
    n = int(input('Digite um numero inteiro para jogar Par ou Impar: '))
    resultado = n + comp
    opcao = ' '
    print('-=|*|=-' * 3)
    while opcao not in 'pPiI':
        opcao = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voce Jogou {n} o computador jogou {comp} e o resultado foi {resultado} ')
    print('Deu Par' if resultado % 2 == 0 else 'Deu Impar')
    if opcao == 'P':
       if resultado % 2 == 0:
          print(f'Voce Ganhou! {n}\n e o PC jogou {comp} resultado foi de {resultado}')
          cont += 1
       else:
           print(f'Voce Perdeu! {n} e o PC jogou  {comp} resultado foi de {resultado}')
           break
    elif opcao == 'I':
         if resultado % 2 == 1:
            print(f'Você Ganhou! {n} e o numero {comp} o resultado foi {resultado}')
            cont += 1
         else:
            print(f'Voce Perdeu')
            break
    print('vamos jogar novamente')
print(f'Game Over você venceu {cont} vezes')