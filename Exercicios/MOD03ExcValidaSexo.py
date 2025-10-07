''''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

print('-=0=-'*6,'MOD 03 EXC  - VALIDADOR DE SEXO','-=0=-'*6)
sexo = str(input('Digite seu sexo: ')).strip().upper()[0]

while sexo != 'Mm' and sexo != 'Ff':
      sexo = str(input('Dados inválidos, Por Favor, Digite seu sexo [M/F]: '))
      print('{}'.format(sexo))

print('Sexo registrado com sucesso !')

print('-=0=-'*6,'MOD 03 EXC  - VALIDADOR DE SEXO','-=0=-'*6)