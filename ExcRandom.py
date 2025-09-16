# faça um programa que leia o nome dos alunos sortear 1 aluno
import random
n1 = str(input('Digite o nome do primeiro Aluno: '))
n2 = str(input('Digite o nome do segundo Aluno: '))
n3 = str(input('Digite o nome do terceiro Aluno: '))
n4 = str(input('Digite o nome do quarto Aluno: '))

lista = [n1,n2,n3,n4]

print ('O Aluno sorteado é: {}'.format(random.choice(lista)))

# sortear ordem de apresentação dos trabalhos
random.shuffle(lista)

print('A ordem da apresentação será: {}'.format(lista))


