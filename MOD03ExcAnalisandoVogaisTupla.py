print('='*6,'MOD 03 EXC - EXTRAINDO VOGAIS DA TUPLA','='*6)

palavra = ('computador','programacao','medico','hospital','usuario')

for c in palavra:
    print(f'\n Na Palavra {c.upper()} temos as vogais:',end=' ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')

print('\n','='*6,'MOD 03 EXC - EXTRAINDO VOGAIS DA TUPLA','='*6)
