print('='*6,'MOD 03 - EXC NÚMEROS EXTENSOS','='*6)


extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')
while True:
    n = int(input('Digite um numero de 0 a 10: '))
    if 0 <= n <= 10 :
        print(f'Você digitou: {extenso[n]}')
        nvo = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        while nvo not in 'nNSs':
            nvo = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if nvo in 'Nn':
            break
    else:
        print('Você Digitou um número inválido, tente novamente')














'''
        while nvo not in 'SN':
            nvo = str(input('Deseja continuar? [S/N] '))
            if nvo == 'N':
                break
'''

