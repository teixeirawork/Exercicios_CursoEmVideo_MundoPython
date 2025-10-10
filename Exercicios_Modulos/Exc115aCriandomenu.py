from pathlib import Path
import funcoes.menu as menu
import funcoes.dados as dados
import time
import aquivos as a

BASE = Path(__file__).parent  # pasta Exercicios_Modulos
arq = BASE / 'aquivos' / 'cadastro.txt'   # caminho correto para Exercicios_Modulos/cadastro.txt

if not a.existeArquivo('cadastro.txt'):
    a.criarArquivo('cadastro.txt')
    
while True:
    resposta  = menu.Guamenu(['Mostrar Pessoas Cadastradas','Cadastrar Novas Pessoas','Sair do Sistema'])
        
    if resposta == 1:
        # mostrar pessoas cadastradas
        
        menu.cabeçalho('\033[35mPessoas Cadastradas\033[m ')    
        print(a.lerArquivo(arq))
        continue
        
    elif resposta == 2:
        # cadastrar novas pessoas
        
        menu.cabeçalho('\033[35mCadastradar Pessoas \033[m')
        nome = str(input('\033[35mnome: \033[m\033[30m'))
        print('\033[m')
        idade = dados.leiaInt('\033[35midade: \033[m\033[30m')
        print('\033[m')
        a.cadastrar(arq,nome,idade)
        print(menu.linha())
        
    elif resposta == 3:
        print('\033[35mSaindo do Sitema! \033[m')
        print(menu.linha())
        break
    else:
        print('Erro! Digite uma opcao Válida!')
    time.sleep(1)  # import time
    