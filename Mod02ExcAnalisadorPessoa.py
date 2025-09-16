# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

print('-='*6,'MOD 02 - EXC ANALISADOR DE PESSOAS','-='*6)

somaidade = 0
hvelho = 0
idvelho = 0
qtmulher = 0

for c in range(1,5):
    print('-='*4, 'DIGITE OS DADOS DA {}º PESSOA','-='*4)
    nome = input('Digite seu nome: ').upper()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo (M/F): ').upper()

    if c == 1 and sexo == 'M':
        hvelho = nome
        idvelho = idade
        somaidade = idade

    elif c == 1 and sexo == 'F' and idade < 20:
            qtmulher += 1
            somaidade = idade

    elif c == 1 and sexo == 'F' and idade > 20:
            somaidade = idade

    elif idade > idvelho and sexo == 'M':
            hvelho = nome
            idvelho = idade
            somaidade += idade

    elif idade < idvelho and sexo == 'M':
            somaidade += idade

    elif sexo == 'F' and idade <= 20:
        qtmulher += 1
        somaidade += idade

    elif sexo == 'F' and idade > 20:
        somaidade += idade

mediaidade = somaidade/4

print('O homem mais velho tem {} anos e seu nome é: {}'.format (idvelho,hvelho))
print('A quantidade de mulheres com idade menor que 20 é: {}'.format(qtmulher))
print('A média das idade é igual a: {}'.format(mediaidade))

print('-='*6,'MOD 02 - EXC ANALISADOR DE PESSOAS','-='*6)
