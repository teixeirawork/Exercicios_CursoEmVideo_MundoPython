##Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.


print('-=|*|=-' * 6, 'MOD 03 - EXC ANALISANDO NÚMEROS E MOSTRANDO SUA MÉDIA','-=*=-'*6)

resp = 'sS'
cont = media = maior = menor = 0
while resp in 'sS':
    n = int(input('Digite um numero: '))
    cont += 1
    media += n
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n


media = media / cont
print('A media dos números digitados foi: {:.2f} e a quantidade de números digitados foi: {} '.format(media, cont))
print('O maior numero foi: {} e o menor número foi {}'.format(maior,menor))
print('-=|*|=-' * 6, 'MOD 03 - EXC ANALISANDO NÚMEROS E MOSTRANDO SUA MÉDIA','-=*=-'*6)
