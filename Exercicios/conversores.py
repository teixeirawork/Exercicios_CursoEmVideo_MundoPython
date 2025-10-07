#conversor
metros = float(input('Digite uma Distancia em metros: '))
km = metros / 1000
cm = metros * 100
mm = metros * 1000
print('A medida de {}m corresponde a \n{}km  \n{}cm.'.format(metros,km,cm))

#tabuada
numero = int(input('Digite um numero para ver sua tabuada: '))
print('{} x {} = {}'.format(numero,1,numero*1))
print('{} x {} = {}'.format(numero,2,numero*2))
print('{} x {} = {}'.format(numero,3,numero*3))
print('{} x {} = {}'.format(numero,4,numero*4))
print('{} x {} = {}'.format(numero,5,numero*5))
print('{} x {} = {}'.format(numero,6,numero*6))
print('{} x {} = {}'.format(numero,7,numero*7))
print('{} x {} = {}'.format(numero,8,numero*8))
print('{} x {} = {}'.format(numero,9,numero*9))
print('{} x {} = {}'.format(numero,10,numero*10))

# conversor de Moedas

valor = float(input('Digite um quanto voce tem na carteira R$: '))
print('voce pode comprar {:.2f} Dollares U$:  '.format(valor / 5.75))

# conversor de temperatura celsius para fahrenheit

cel = float(input('Digite a temperatura em celsius: '))
fah = ((9*cel)/5)+32
print('A temperatura de {}ºC corresponde a ´{} ºF '.format(cel,fah))