##Exercício Python 37:
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a
# base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('=============EXC Conversor de Bases ===================')
base = int(input('Digite um numero inteiro para converter as Bases: '))
print ('[1] - Binario: \n [2]- Octal: \n [3]- Hexadecimal:')
opcao =int(input('Digite a opção desejada para converter as Bases: '))
print('=============EXC Conversor de Bases ===================')

if opcao == 1:
    base = bin(base)
    print (base[2:])
elif opcao == 2:
    base = oct(base)
    print (base[2:])
else:
    base = hex(base)
    print (base[2:])


