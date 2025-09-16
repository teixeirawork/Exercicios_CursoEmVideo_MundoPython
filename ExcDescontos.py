# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

valorproduto = float(input('Digite o valor do produto R$: '))
valordesconto = valorproduto * 5/100
valorfinal = valorproduto - valordesconto
print('o valor do desconto R$: {}\n valor final do produto R$: {} '.format(valordesconto, valorfinal))

# Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

salario = float(input('Digite o valor do salario R$: '))
aumento = salario * 0.15
valorfinal = salario + aumento
print('o valor do salario {} o valor do aumento {}'.format(salario, valorfinal))