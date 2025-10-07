# FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE UM NUMERO SOLICITADO NA TELA


print('-='*6,'MOD 02 EXC  - TABUADA','-='*6)

n = int(input('Digite um numero para tabuada: '))

for c in range(0,11):
    print('{} x {:2} = {}'.format(n,c,n*c))

print('-='*6,'MOD 02 EXC  - TABUADA','-='*6)


print('-='*6,'MOD 02 EXC  - SOMA DOS PARES','-='*6)
# FAÇA UM PROGRAMA QUE LEIA 2 NÚMEROS E SOME CASO ELES FOREM PARES, CASO VALOR SEJA IMPAR DESCONSIDERE


soma =  0
cont = 0
impar = 0
for c in range(0,7):
    n = int(input('Digite um numero 1: '))
    if n % 2 == 0:
       soma += n
       cont += 1
    else:
            print ('numero impar detectado')
            impar += 1
print ('soma dos números pares é igual a: {}\n a contagem dos numeros pares é: {}\n'.format(soma,cont), end='')
print('quantidade de numeros impares: {}\n'.format(impar))

print('-='*6,'MOD 02 EXC  - SOMA DOS PARES','-='*6)