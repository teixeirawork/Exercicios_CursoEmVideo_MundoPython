# #Exercício Python 115a: Vamos criar um menu em Python, usando modularização.

##c= ('\033[m',        # 0 - sem cor
#    '\033[31m', # - vermelho
#    '\033[32m', # - verde
#    '\033[33m', # - amarelo 
#    '\033[34m', # - azul - escuro    
#    '\033[35m', # - roxo
#    '\033[36m', # - azul - claro
#    '\033[37m', # - branco
#       A PARTIR DAQUI FAZ FUNDO DE COR COM LETRA BRANCA SEGUINDO ESCALA ACIMA
#    '\033[40m',# - VERMELHO
#    '\033[41m',# - VERDE
#    '\033[42m',# - AMARELO

#)

def linha(tam = 40):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())

def Guamenu(lista):
    import funcoes.dados as dados    
    cabeçalho('\033[35mMENU INTERATIVO\033[m')
    c = 1
    for item in lista:
        print(f'\033[35m{c} - \033[m\033[30m{item}\033[m')
        c += 1
    print(linha())
     
    opcao = dados.leiaInt('\033[35mSua Opção: \033[m\033[0;30m')
    print('\033[m')
    return opcao
    
 
 
 

def Texmenu(opcao = 0):
    print('-'*30)
    print('\t\033[0;35mMENU INTERATIVO\033[m')
    print('-'*30)
    
    print('\033[0;35m1 - \033 \033[0;30mVer pessoas cadastradas\033[m')
    print('\033[0;35m2 - \033 \033[0;30mCadastrar novas pessoas\033[m')   
    print('\033[0;35m3 - \033\033[0;30mSair do Sistema\033[m')
    print('-'*30)    
    while True:
        entrada = str(input('\033[0;35mOpção:\033[m \033[0;30m')).strip()
        print(' \033[m')
        if entrada =='':
            print('\033[0;31mErro! Digite uma opcao valida.\033[m')
            continue

        if entrada == '1':
            print('-'*30)
            print('\tOPCAO 1')
            print('-'*30)
            continue
            
        if entrada == '2':
            print('-'*30)
            print('\tOPCAO 2')
            print('-'*30)
            continue

        if entrada == '3':
            print('-'*30)
            print('\tSAINDO DO SISTEMA')
            print('-'*30)
            break    
        try:
            opcao = int(entrada)
            if entrada != 1 or entrada != 2 or entrada !=3:
                print('\033[0;31mErro! Digite uma opcao valida.\033[m')
            continue        
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite uma opção valida.\033[m')
            continue    
        except KeyboardInterrupt:
            print('\033[0;31mErro! O Usuário preferiu não informar nenhum numero!.\033[m')
            continue
        
    return opcao
            