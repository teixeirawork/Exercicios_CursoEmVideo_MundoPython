##Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.


print('-=|*|=-' * 6, 'MOD 03 - EXC TABUADA COM BREAK NEGATIVO','-=*=-'*6)


while True:
    n = int(input('Digite um valor pra ver sua tabuada: '))
    if n < 0:
        break
    print('-=|*|=-' * 6)
    for c in range(0, 11):
        print(f'{n} x {c} = {n * c}')

    print('-=|*|=-' * 6)

print('-=|*|=-' * 6, 'MOD 03 - EXC TABUADA COM BREAK NEGATIVO','-=*=-'*6)