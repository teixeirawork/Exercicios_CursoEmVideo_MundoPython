#ESCREVA UM PROGRAMA QUE LEIA UMA QUATIDADE DE NUMERO, E FAÇA SUA PROGRESSAO ARITIMÉTICA

print('-='*6,'MOD 02 EXC  - PROGRESSÃO ARITIMÉTICA','-='*6)

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for c in range (termo,decimo + razao,razao):
    print('{}'.format(c),end='-> ')
print('FIM')

print('-='*6,'MOD 02 EXC  - PROGRESSÃO ARITIMÉTICA','-='*6)