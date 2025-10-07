#Exercício Python 038:
#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
print('================= MOD 02 - EXC COMPARADOR DE NUMEROS =============')
primeiro = int(input('Escreva o primeiro valor: '))
segundo = int(input('Escreva o segundo valor: '))
print('================= MOD 02 - EXC COMPARADOR DE NUMEROS =============')

if primeiro > segundo:
    print('Primeiro valor é maior')
elif segundo > primeiro:
    print('Segundo valor é maior')
else:
    print('Os dois números são iguais')