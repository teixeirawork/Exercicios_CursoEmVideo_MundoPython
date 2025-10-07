print ("=========================== MOD 02 EXC GERENCIADOR DE PAGAMENTOS =======================")

##Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

vlrprod = float(input('digite o valor do produto: '))
print('[1] - à vista dinheiro/cheque\n'
      '[2] - à vista cartão\n'
      '[3] - 2x no cartão\n'
      '[4] - 3x no cartão\n')
formapgo = int(input('Digite a forma de Pagamento que deseja utilizar: '))

if formapgo == 1:

    desc = vlrprod * 0.10
    vlrtotal = vlrprod - desc

    print('Valor Do Produto {:.2f}\n'
          'Valor do desconto {:.2f}\n'
          'Valor Total da Compra {:.2f}'.format(vlrprod, desc,vlrtotal))
elif formapgo == 2:
    desc = vlrprod * 0.05
    vlrtotal = vlrprod - desc

    print ('Valor do Produto {:.2f}\n'
           'Valor do Desconto {:.2f}\n'
           'Valor Total da Compra {:.2f}'.format(vlrprod, desc,vlrtotal))
elif formapgo == 3:
    vlrtotal = vlrprod

    print('Valor do Produto {:.2f}\n'
          'Valor Total da Compra {:.2f}'.format(vlrprod, vlrtotal))

elif formapgo ==4:
     acre = vlrprod * 20 / 100
     vlrtotal = vlrprod + acre
     print ('Valor do produto R$ {:.2f}\n'
           'Valor do desconto {:.2f}\n'
           'Valor Total da Compra {:.2f}'.format(vlrprod, acre,vlrtotal))
else:
        print('Digite uma opção valida')
        
print ("=========================== MOD 02 EXC GERENCIADOR DE PAGAMENTOS =======================")