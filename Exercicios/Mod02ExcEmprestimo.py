##Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


print("=======SIMULADOR DE EMPRÉSTIMOS=========")
casa = float(input('digite o valor da sua casa R$: '))
salario = float(input('Digite o seu salario R$: '))
tempo = int(input('digite o tempo em meses que deseja pagar: '))
print("=======SIMULADOR DE EMPRÉSTIMOS=========")

anos = tempo * 12
vlrparcela = casa / anos
minimo = salario * 30 / 100

print('Para pagar uma casa no valor de R$: {:.2f} em {:.2f} anos '.format(casa, anos), end='')
print('O valor da parcela será R$: {:.2f}'.format(vlrparcela))

if vlrparcela <= minimo:
 print('Emprestimo Aprovado!')
else:
   print('Emprestimo Reprovado!')


   # expressão end = '' = comando para fazer os 2 print's aparecer na mesma linha