##Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:

print('-='*6,'MOD 02 - EXC PALÍNDROMOS','-='*6)

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

## inverso = junto[::-1] maneira de inverter uma palavra estripando uma string
# com essa declaração o próprio python inverte a frase sem precisar do laço for

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('A frase invertida é: '.format(junto,inverso))
if inverso == junto:
    print('A frase é um Palíndromo!')
else:
    print('A frase não é um Palíndromo')

print('-='*6,'MOD 02 - EXC PALÍNDROMOS','-='*6)