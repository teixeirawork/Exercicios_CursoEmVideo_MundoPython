# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita
# que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = list()
media = 0
while True:

    """
    nome = str(input('Nome do Aluno: ')).upper().strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))

    alunos.append(nome)
    alunos.append(n1)
    alunos.append(n2)
    media = (n1 + n2) / 2
    alunos.append(media)


    """
# GUANABARA
    nome = str(input('Nome do Aluno: ')).upper().strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    alunos.append([nome, [n1, n2],media])

    resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    while resp not in 'SN':
       resp = str(input('Opção inválida! deseja continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break


print('--------------- BOLETIM ---------------')
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 30)
"""
for i in range(0, len(alunos),4):
    print(f'{alunos.count(i)} {alunos[i]:^15}{alunos[i+3]:>15}')
    print('-' * 30)
"""
# exercicio do guanabara

for i, a in enumerate(alunos):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8}')
    print('-' * 30)
while True:
    print('='*35)
    opc = int(input('Mostrar notas de qual aluno? (999 para parar): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(alunos) - 1:
        print(f'Notas do aluno {alunos[opc][0]} são {alunos[opc][1]} ')

    resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Opção inválida! deseja continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break


