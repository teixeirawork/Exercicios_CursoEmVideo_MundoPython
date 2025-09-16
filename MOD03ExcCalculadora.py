'''

Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
'''

print('-=*=-'*6,'MOD 03 EXC  - VALIDADOR DE SEXO','-=*=-'*6)


opcao = 0

print('-=|*|=-'*3,'TexCalculator', '-=|*|=-'*3)

while opcao != 8:
    primeiro = int(input('Digite o primeiro valor: '))
    segundo = int(input('Digite o segundo valor: '))

    print('-=|*|=-'*3)
    opcao = int(input('Digite qual operação Deseja utilizar: \n'
                      '[1] - Somar \n'
                      '[2] - Multiplicar \n'
                      '[3] - Diminuir \n'
                      '[4] - Didividir \n'
                      '[5] - Fatorial Errado \n'
                      '[6] - Fatorial Correto \n'
                      '[7] - Progressão Aritmética \n'
                      '[8] - Sair do programa \n'))
    print('-=|*|=-'*3)
    if opcao == 1:
        resultado = primeiro + segundo
        print('O resultado da soma: {}'.format(resultado))
        print('-=|*|=-' * 3)
    elif opcao == 2:
        resultado = primeiro * segundo
        print('O resultado da multiplicação: {}'.format(resultado))

        print('-=|*|=-' * 3)
    elif opcao == 3:
        resultado = segundo - primeiro

        print('O resultado da subtração: {}'.format(resultado))

        print('-=|*|=-' * 3)

    elif opcao == 4:
        resultado = primeiro / segundo
        print('O resultado da divisão: {}'.format(resultado))
        print('-=|*|=-' * 3)

    elif opcao == 5:
            resultado = 0
            for c in range (primeiro, 0 , -1):
                print('{} x {}'.format(primeiro, c))
                if resultado == 0:
                    resultado = primeiro * c
                elif resultado != 0:
                    resultado *= c
                if c == 1:
                    print('O resultado é: {}'.format(resultado))

    elif opcao == 6:    
        ''''
        -==-=-=-=-=-=-=-=-= OUTRA FORMA MAIS SIMPLES DE OBTER O RESULTADO DE FACTORIAL =-=--=-
        from math import factorial
        n = int(input('Digite um numero para ver seu Fatorial))
        f = factorial(n)
        print('O fatorial de {} é {}'.format(n, f))')
        -==-=-=-=-=-=-=-=-= OUTRA FORMA MAIS SIMPLES DE OBTER O RESULTADO DE FACTORIAL =-=--=-       
        '''
        from math import factorial
        c = primeiro
        f = 1
        print('Calculando o: {}! \n'.format(primeiro))
        while c > 0:
            print('{}'.format(c),end='')
            print('x' if c > 1 else ' = {}'.format(c), end='')
            c -= 1
            print('{}'.format(factorial(primeiro)))

    elif opcao == 7:
        termo = primeiro
        razao = segundo
        cont = 1
        total = 0
        maistermos = 10
        while maistermos != 0:
            total = total + maistermos
            while cont <= total:
                print('{}->'.format(termo),end='')
                termo += razao
                cont += 1
            print('PAUSA')
            print('-=|*|=-' * 3)
            maistermos = int(input('Digite mais quantos termos deseja mostra: '))
        print('-=|*|=-' * 3)
        print('A quantidade de termos mostrada é: {}'.format(total))
        print('-=|*|=-' * 3)
    elif opcao == 8:
        print('Desligando Calculadora ...')

print('-=|*|=-'*3,'TexCalculator', '-=|*|=-'*3)
print('-=*=-'*6,'MOD 03 EXC  - VALIDADOR DE SEXO','-=*=-'*6)