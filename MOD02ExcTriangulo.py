print ('=========================== MOD 02 EXC TRIANGULOS=======================')
# CRIE UM PROGRAMA QUE ANALISA SE AS MEDIDAS DO SEGMENTO FORMAM UM TRIANGULO
# E DEPOIS DIGA QUAL TIPO DE TRIANGULO É FORMADO
#

seg1 = int(input('digite o primeiro segmento: '))
seg2 = int(input('digite o segundo segmmento: '))
seg3 = int(input('digite o terceiro segmento: '))


if seg1 < seg2 + seg3 and seg1 < seg1 + seg3 and seg3 < seg2 + seg1:
   if seg1 < seg2 + seg3 and seg2 < seg3 + seg1 and seg3 < seg1 + seg2:
       print('Os segmentos formam um triangulo')
   if seg1 == seg2 == seg3:
            print('Esses segmentos formam um Triângulo Equilátero\n')
   if seg1 != seg2 != seg3 != seg1:
            print('Esses segmentos formam um Triângulo Escaleno\n')
   else:
            print('Esses segmentos formam um Triângulo Isósceles')

else:
   print('os segmentos nao forma triangulo')

print ('=========================== MOD 02 EXC TRIANGULOS=======================')