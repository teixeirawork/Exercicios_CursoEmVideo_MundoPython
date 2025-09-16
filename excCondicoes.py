# ESCREVA UM PROGRAMA QUE TENTA FAÇA O COMPUTADOR PENSAR EM UM NUMERO DE 0 A 5
# PEÇA PARA O USUARIO TENTAR ADIVINHAR QUAL NUMERO ESCOLHIDO
# ESCREVA SE ACERTOU OU NAO

import random
from random import triangular

num = random.randint(1,5)
usr = int(input('Digite um numero entre 1 e 5: '))
if num == usr:
    print('voce acertou!')
else:
    print('voce errou!')

### calcula multa

vel = int(input('Digite a velocidade do Carro:'))
if vel > 80:
    multa = (vel - 80) * 7
    print('valor da multa é : {}'.format(multa))
else:
    print('Voce é um bom motorista Parabens')


### escreva se é impar ou par

num = (int(input('Digite um numero para saber se é impar ou par: ')))
if num % 2 == 0:
    print('Par')
else:
    print('Impar')

## calcula viagens, de 200 km a 0,50 e viagems acima a 0.45

km = float(input('Digite a quantidade de km percorrida: '))
if km <= 200:
    ps = km * 0.50
    print ('o valor da passagem é: {:2f}'.format(ps))
else:
    ps = km * 0.45
    print('o valor da passagem é : {:2f}'.format(ps))

import datetime
## verifica ano BISsEXTO
ano = int(input('Digite o ano para saber se é bisexto caso queira o ano atual digite 0 : '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('ano bisexto')
else:
    print('ano nao bisexto')

## programa que leia 3 segmentos e diga se formam um triangulo

seg1 = float(input('Digite o seguimento 1: '))
seg2 = float(input('Digite o seguimento 2: '))
seg3 = float(input('Digite o seguimento 3: '))

if seg1 < seg2 + seg3 and seg2 < seg3 + seg1 and seg3 < seg1 + seg2:
    print('Os segmentos formam um triangulo')
    if seg1 == seg2 == seg3:
        print('Esses segmentos formam um Triângulo Equilátero')
    if seg1 != seg2 and seg2 !=seg3 and seg1 != seg3:
        print('Esses segmentos formam um Triângulo Escaleno')
    else:
        print('Esses segmentos formam um Triângulo Isósceles')

else:
    print('nao forma triangulo')