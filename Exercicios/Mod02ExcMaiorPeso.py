# Faça um programa que leia o peso de cinco pessoas. No final,
# mostre qual foi o maior e o menor peso lidos.


print('-='*6,'MOD 02 - EXC MAIOR E MENOR PESO','-='*6)

maior = 0
menor = 0

for c in range(1,6):
    peso = float(input('Digite o peso da {}º pessoa em kg: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso

    elif peso > maior:
         maior = peso

    elif peso < menor:
         menor = peso

print('maior peso: {}'.format(maior))
print('menor peso: {}'.format(menor))
print('-='*6,'MOD 02 - EXC MAIOR E MENOR PESO','-='*6)
