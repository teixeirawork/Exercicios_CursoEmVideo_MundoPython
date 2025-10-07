## CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE
# O NOME COM TODAS AS LETRAS MAIUSCULAS
# O NOME COM TODAS AS LETRAS MINUSCULAS
# QUANTAS LETRAS TEM O NOME SEM CONSIDERAR ESPAÇOS
# QUANTAS LETRAS TEM O PRIMEIRO NOME

nomecompleto = str(input('Digite o nome completo: ')).strip()
print('o seu nome em Maiusculas: ', nomecompleto.upper())
print('o seu nome em Minusculas: ',nomecompleto.lower())
print('a quantidade de Letras do seu nome é: {}'.format(len(nomecompleto) - nomecompleto.count(' ')))
print(len(nomecompleto.strip())) # apenas começo e incio da frase palavra, ver como estripar o meio
primeironome = nomecompleto.split()
print('Seu primeiro nome é',(primeironome[0]))
print ('Seu Ultimo nome é {}'.format(primeironome[len(primeironome)-1]))

# crie um programa que leia o nome de uma cidade e verifique se ela começa ou nao com nome de santo

cid = str(input('Digite o nome da cidade: ')).upper().strip()
print(cid[:5] == 'SANTO')
print(cid.find('SANTO'))
print("SANTO" in cid)

# leia uma frase pelo teclado e mostre quantas vezes a letra "A" aparece, onde ela aparece por ultimo e primeiro
frase = str(input('Digite uma frase: ')).strip().upper()
print('A quantidade de vezes que a letra A aparece é: {}'.format(frase.count('A')))
print('a primeira letra A posição: {}'.format(frase.find('A')+1))
print ('a ultima ocorrencia de A: {}'.format(frase.rfind('A')+1))

