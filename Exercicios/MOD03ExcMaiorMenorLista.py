"""
lista = [10, 20, 30, 40, 50]
print(lista)
print('='*4)

lista.sort(reverse=True)
print(lista)
print('='*4)

lista.append(60)
print(lista)
print('='*4)

lista.insert(2, 70)
print(lista)
print('='*4)

lista.pop(6) # remove pelo index
print(lista)
print('='*4)

lista.remove(70) # remove o primeiro conteúdo encontrado
print(lista)
print('='*4)

valores = list()
valores.append(10)
valores.append(5)
valores.append(4)
valores.append(3)

for c, v in enumerate(valores):
    print(f'Na posição: {c} encontrei valores = {v}')
print('fim da lista')
"""

## faça um programa que leia 5 valores pelo teclado e diga, qual o maior valor e qual foi o menor com a suas posições

"""
MANEIRA QUE EU FIZ SEM FOR

valores = [int(input('Digite o 1º Valor: ')),
           int(input('Digite o 2º Valor: ')),
           int(input('Digite o 3º Valor: ')),
           int(input('Digite o 4º Valor: ')),
           int(input('Digite o 5º Valor: '))]

print(f'Os númros Digitados foram: {valores}')
print(f'O Maior valor digitado foi: {max(valores)} e esta na posição: {valores.index(max(valores))+1}')
print(f'O menor valor digitado foi: {min(valores)} e esta na posição: {valores.index(min(valores))+1}')
"""


# MANEIRA GUANABARA EXERCICIO COM FOR

maior = menor = 0
valores = list()
for v in range(0, 5):
    valores.append(int(input(f'Digite o {v+1}º Valor: ')))
    if v == 0:
        maior = valores[v]
        menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print('='*10)
print(f'Os valores digitados foram: {valores}')
print('='*10)
print(f'O maior valor digitado foi: {maior} nas posições: ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i+1}...', end='')
print()
print(f'O menor valor digitado foi: {menor} nas posições: ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i+1}...', end='')

