val = list(range(1,5))
print(val)

pessoas = [['Pedro', 25], ['Maria', 12], ['José', 25]]
print(pessoas[2][1])


letras = ('J', 'X', 'M', 'O', 'A', 'K')

print(letras.index('A'))

num = [3, 6, 4, 1]
for n1, n2 in enumerate(num):
    print(n1 + n2,end='')
print()
    
print('ultima questao')   
num = [2, 8, 4, 7]
num.pop()
num.insert(1, 3)
num.append(6)
print(num)