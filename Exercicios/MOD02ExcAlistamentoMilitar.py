##Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


print('================== MOD 02 - EXC ALISTAMENTO MILITAR ======================')

import datetime

anonasc = int(input(' Digite o seu ano de nascimento: '))
anoatual = datetime.date.today().year
idade = anoatual - anonasc
if idade == 18:
    print('Você possui {} anos Já é hora de se alistar'.format(idade))
elif idade < 18:
    alistamento = 18 - idade
    anoalistamento = anoatual + alistamento
    print('Ainda é cedo você possui {} anos!, ainda falta {} anos para você se alistar'.format(idade,alistamento))
    print('Você se alistará no ano de {}'.format(anoalistamento))
else:
    atraso = idade - 18
    ideal = anoatual - atraso
    print('Você possui {} anos!,\n Deveria se apresentar em {}\n Está atrasado {} anos \n está atrasado corra se apresentar!'.format(idade,ideal,atraso))

print('================== MOD 02 - EXC ALISTAMENTO MILITAR ======================')