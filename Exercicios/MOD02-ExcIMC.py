print ('=========================== MOD 02 EXC IMC =======================')
# FAÇA UM PROGRAMA QUE LEIA O PESO E A ALTURA DAS PESSOAS E DIGA SE
# QUAL O GRAU DE MASSA CORPORAL QUE ELA TEM
# 18.5 ABAIXO DO PESO       # 25 ATÉ 30 SOBREPESO   # 40 PRA CIMA OBESIDADE MÓRBIDA
# 18.5 ATÉ 25 PESO IDEAL    # 30 ATÉ 40 OBESIDADE


peso = float(input('Digite o peso em Kg: '))
altura = float(input('Digite o altura em m: '))
imc = peso / (altura * altura)
print('seu imc é igual a: {:.1f}'.format(imc))

if imc <= 18.5:
    print('abaixo do peso')
elif 18.5 <= imc <= 25:
    print('peso ideal')
elif 25 <= imc <= 30:
    print('sobrepeso')
elif 30 <= imc <= 40:
    print('obesidade')
else:
    print('obesidade')


print ('=========================== MOD 02 EXC IMC =======================')