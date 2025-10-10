def lerArquivo(nome):
    try:
        with open(nome,'rt', encoding='utf-8') as a:
            for linha in a:
                dado = linha.strip().split(';')
                # evita IndexError se a linha não tiver dois campos   
                nome_cad = dado[0] if len(dado) > 0 else ''
                idade_cad = dado[1] if len(dado) > 1 else''
                print(f'\033[35m{nome_cad:<30} \t{idade_cad:>3}\033[m')
    except FileNotFoundError: 
        print(f'Arquivo não encontrado! {nome}')
    except OSError as e:
        print(f'Erro ao ler/abrir o arquivo: {e}')
    

def existeArquivo(nome):
    try:
        with open(nome,'rt', encoding='utf-8') as a:
            return a.read()
    except FileExistsError:
        print(f'Arquivo já foi criado! {nome}')
    return None

def criarArquivo(nome):
    try:
        with open(nome,'wt+', encoding='utf-8') as a:
            a.write(nome) 
    except:
        print('Houve um erro na criaçao do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
        
        
def cadastrar(arq,nome='desconhecido',idade='0'):
    try:
        with open(arq, 'at', encoding='utf-8') as a:
            a.write(f'{nome};{idade} anos\n')
    except:
        print('Hove um erro ao abrir o arquivo!')
    else:
        print(f'Novo registro de {nome} adicionado')        