# Exercício Python 086:
# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para: [{l},{c}]: '))

linha2 = coluna3 = somapar = 0
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if matriz[1][c] != ' ':
            linha2 = matriz[1][c]
            if linha2 < matriz[1][c]:
                linha2 = matriz[1][c]

    if matriz[l][2] != '':
       coluna3 += matriz[l][2]

    print()
print(f'A soma dos valores pares: [{somapar}]')
print(f'A soma dos valores da terceira coluna: [{coluna3}]')
print(f'O maior valor da segunda linha: [{linha2}]')