##Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


print('-='*6,'MOD 02 - EXC GRUPO MAIORIDADE','-='*6)

from datetime import date
maior = 0
menor = 0
for c in range (0,7):

    ano = int(input('Digite o ano de nascimento: {}º pessoa: '.format(c+1)))
    idade = date.today().year - ano

    if ano > date.today().year:
        print ('Ano errado')
        c -= 1

    if idade <= 17 and ano < date.today().year:
       menor += 1
    else:
        maior += 1

print('A quantidade de pessoas Maiores de idade é: {}'.format(maior))
print('A quantidade de pessoas Menores de idade é: {}'.format(menor))

print('-='*6,'MOD 02 - EXC GRUPO MAIORIDADE','-='*6)