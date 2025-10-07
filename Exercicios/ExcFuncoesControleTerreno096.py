def area(largura, comprimento):
    terreno = largura * comprimento
    print(f'A area de um terreno {largura} x {comprimento} = {terreno:.2f}m²')
    
    
print('-'*15,'CONTROLE DE TERRENOS','-'*15)
print('-'*60)
larg = float(input('LARGURA (m): '))
compr = float(input('Comprimento (m): '))

area(larg, compr)