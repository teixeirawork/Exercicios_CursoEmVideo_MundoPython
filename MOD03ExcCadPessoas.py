##Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

cont = maior18 = mulher = homem = 0
while True :
    idade = int(input('Digite sua idade: '))
    sexo =  str(input('Digite seu sexo (M/F): ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo (M/F): ')).upper().strip()[0]
    if sexo == 'M':
        homem += 1
        cont += 1
    elif sexo == 'F' and idade < 20:
        mulher += 1
        cont += 1
    elif idade > 18:
        maior18 += 1
        cont += 1
    else:
        cont += 1
    resp = str(input('Deseja Cadastrar outra pessoa? [S/N]')).upper().strip()[0]
    while resp not in 'NS':
        resp = str(input('Deseja Cadastrar outra pessoa? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break

print(f'A quantidade de pessoas cadastradas: {cont}')
print(f'A quantidade de mulheres cadastradas com menos de 20 anos: {mulher}')
print(f'A quantidade de Homens cadastrados foram: {homem}')
print(f'A quantidade de Pessoas maiores de 18: {maior18}')







'''
cont = maior18 = mulher = homem = 0

'''

