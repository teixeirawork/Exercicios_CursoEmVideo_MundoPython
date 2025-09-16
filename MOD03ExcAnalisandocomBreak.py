##Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)

print('-=|*|=-'*6,'MOD 03 EXC ANALISANDO NUMEROS COM BREAK','-=|*|=-'*6)

cont = soma = 0
while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1


print('---------------')
print(f'A soma dos números: {soma}')
print(f'A quantidade de números: {cont}')
print('---------------')
print('-=|*|=-'*6,'MOD 03 EXC ANALISANDO NUMEROS COM BREAK','-=|*|=-'*6)