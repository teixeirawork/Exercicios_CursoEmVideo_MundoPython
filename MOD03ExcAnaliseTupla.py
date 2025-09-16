


print('-=|*|=-' * 3,'MOD 03 EXC ANÁLISE TUPLA ','-=|*|=-' * 3)

par = nove = pos = 0
vlr = (int(input('Digite 1 valor: ')),int(input('Digite 2 valor: ')),int(input('Digite 3 valor: ')),int(input('Digite o 4 valor: ')))

for i in vlr:
    if i % 2 == 0:
        par += 1
    if i == 3:     # vlr.index(3)+1 -> MOSTRA A POSIÇÃO INDEX DE ONDE O NUMERO 3 APARECE NA TUPLA
        pos += 1
        pos = vlr.index(i)+1
    if i == 9:      # vlr.count(9) -> CONTA QUANTAS VEZES O VALOR 9 APARECEU NA TUPLA
        nove += 1

print(f'Quantas vezes o 9 apareceu: {nove}')
print(f'A posição do número 3: {pos}')
print(f'A quantidade de pares é: {par}')

print('-=|*|=-' * 3,'MOD 03 EXC ANÁLISE TUPLA ','-=|*|=-' * 3)
