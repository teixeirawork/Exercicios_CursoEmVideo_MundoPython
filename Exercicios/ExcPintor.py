#Dicas, Nunca tentar resolver o problema de uma vez, tentar encaixar como se fosse peças de lego

#Especificações = para cada 2 m2 é preciso de 1 lt de tinta

largura = float(input('Digite a Largura da sua Parade em m: '))
altura  = float(input('Digite a Altura da sua Parade em m: '))

m2= largura * altura
QtLitros = (m2/2) * 1

print('A dimensão da sua parade é {}x{} e a area equivale a {}m²'.format(largura,altura,m2))
print ('A quantidade de tinta que voce usará para pintar a parede será {}Lts de tinta'.format(QtLitros))