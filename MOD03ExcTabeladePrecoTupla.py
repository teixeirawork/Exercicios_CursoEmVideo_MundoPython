
print('='*6,'MOD 03 EXC - TABELA DE PREÇOS COM TUPLA','='*6)

tab = ('cebola','50','acelga','40','feijao','60','alface','70','arroz','65')

for c in range (0,len(tab)):
    if c % 2 == 0:
        print(f'{tab[c]:.<30}',end='')
    else:
        print(f'R${tab[c]:>3}',end='\n')


print('='*6,'MOD 03 EXC - TABELA DE PREÇOS COM TUPLA','='*6)