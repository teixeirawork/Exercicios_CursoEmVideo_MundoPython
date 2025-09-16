# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa 60 por dia + 0,15 por km rodado

dias = int(input('Quantos dias voce pretende alugar o carro: '))
km = float(input('Quantos km você pretende rodar com o carro: '))

vlrcarro = dias * 60
vlkm = km * 0.15
vlrtotal = vlrcarro + vlkm

print('O Valor do Aluguel sera de R$: {:.2f}'.format(vlrtotal))