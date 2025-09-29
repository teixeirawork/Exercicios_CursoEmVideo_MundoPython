# escreva um programa que faça um print especial que cresce e diminui conforme quantidade de caracteres


def especial(frase):
    contador = len(frase) +4
    print('-' * contador)
    print(f'  {frase}')
    print('-' * contador)
    
    

fras = str(input('Digite uma frase: '))
especial(fras)

fras2 = str(input('Digite outra frase: '))
especial(fras2)

fras3 = str(input('DIgite mais 1 frase: '))
especial(fras3)