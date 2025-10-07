##A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria,# de acordo com a idade:
##  Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER


print('====================== MOD 02 - EXC ATLETA =====================')
import datetime
nome = str(input('Digite o seu nome: '))
anonasc  =  int(input(' Digite o seu ano de nascimento: '))
anoatual = datetime.date.today().year
idade = anoatual - anonasc
if idade <= 9:
    print('O Atleta: {} \n Possui: {} Anos'.format(nome, idade))
    print('Categoria: Atleta Mirim')
elif idade <= 14:
    print('O Atleta: {} \n Possui: {} Anos'.format(nome, idade))
    print('Categoria: Atleta Infantil')

elif idade <= 19:
    print('O Atleta: {} \n Possui: {} Anos'.format(nome, idade))
    print('Categoria: Atleta Junior')
elif idade <= 25:
    print('O Atleta: {} \n Possui: {} Anos'.format(nome, idade))
    print('Categoria: Atleta Sênior')
else:
    print('O Atleta: {} \n Possui: {} Anos'.format(nome, idade))
    print('Categoria: Atleta Master')

print('====================== MOD 02 - EXC ATLETA =====================')