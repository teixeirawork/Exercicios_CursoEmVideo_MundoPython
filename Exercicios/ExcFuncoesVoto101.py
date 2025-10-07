##Exercício Python 101: 
# Crie um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto 
# NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(ano):
    
    from datetime import datetime    
    atual = datetime.now().year
    idade = atual - ano
    
    if idade < 16:
        msg = print(f" sua idade {idade} o voto é negado!")
        return msg
    elif (idade >= 16 and idade < 18) or idade >= 65:
        msg = print(f"A sua idade: {idade} o voto é opcional!")
        return msg
    else:
        msg = print(f"A sua idade: {idade} o Voto Obrigatorio nas eleições")
        return msg   
 
 
 # Programa Principal
 
ano = int(input('Digite o ano de nascimento: '))
voto(ano)

        