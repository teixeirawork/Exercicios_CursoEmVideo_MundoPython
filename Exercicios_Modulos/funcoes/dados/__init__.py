## Exercício Python 113: Reescreva a função leiaInt() 
# que fizemos no desafio 104, 
# incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = input(msg).strip()
            if n == '':
                raise ValueError('Forçar Tratamento de erro!')
            return int(n)     
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um numero inteiro valido.\033[m')
            continue    
        except KeyboardInterrupt:
            print('\033[0;31mErro! O Usuário preferiu não informar nenhum numero!.\033[m')
            return 0 
           
        
        
        


def leiaFloat(msg):
    while True:
        try:
            n = input(msg).strip().replace(',','.')
            if n == '' :
                raise ValueError('Forçar Tratamento de erro!')
            return float(n)
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um numero real valido!.\033[m')    
        except KeyboardInterrupt:
            print('\033[0;31mErro! O Usuário preferiu não informar nenhum numero!.\033[m')
            return 0
       
        
        