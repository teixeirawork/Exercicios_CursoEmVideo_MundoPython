# Exercício Python 083:
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expr = str(input('Digite uma expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
   print('Sua expressão é válida!')
else:
   print('Sua expressão está errada!')

while True:
    opcao = str(input('Deseja Continuar S/N: ')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Deseja Continuar S/N: ')).upper().strip()[0]
    if opcao == 'N':
        break
    else:
         expr = str(input('Digite uma nova expressão: '))
         for simb in expr:
            if simb == '(':
                pilha.append('(')
            elif simb == ')':
                if len(pilha) > 0:
                    pilha.pop()
                else:
                    pilha.append(')')
                    break
    if len(pilha) == 0:
        print('Sua expressão é válida!')
    else:

        print('Sua expressão está errada!')
