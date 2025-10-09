# #Exercício Python 115a: Vamos criar um menu em Python, usando modularização.

##c= ('\033[m',        # 0 - sem cor
#    '\033[0;30;41m', # 1 - vermelho
#    '\033[0;30;41m', # 2 - verde
#    '\033[0;30;41m', # 3 - amarelo    
#    '\033[0;30;41m', # 4 - azul
#    '\033[0;30;41m', # 5 - roxo
#    '\033[0;30;41m', # 6 - branco
#)


def menu(opcao = 0):
    print('-'*30)
    print('\tMENU INTERATIVO')
    print('-'*30)
    
    print('1 - Ver pessoas cadastr')
    print('2 - Cadastrar novas pessoas')   
    print('3 - Sair do Sistema')
    print('-'*30)    
    while True:
        entrada = str(input('Opção: ')).strip()
        if entrada =='':
            print('\033[0;31mErro! Digite uma opcao valida.\033[m')
            continue

        if entrada == '1':
            continue

        if entrada == '2':
            continue

        if entrada == '3':
            break    
        try:
            opcao = int(entrada)
            if entrada != 1 or entrada != 2 or entrada !=3:
                print('\033[0;31mErro! Digite uma opcao valida.\033[m')
            continue        
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um numero inteiro valido.\033[m')
            continue    
        except KeyboardInterrupt:
            print('\033[0;31mErro! O Usuário preferiu não informar nenhum numero!.\033[m')
            return opcao 