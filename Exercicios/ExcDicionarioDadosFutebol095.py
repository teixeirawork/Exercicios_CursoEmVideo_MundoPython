##Exercício Python 095: 
# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.




# - CADASTRO DOS JOGADORES


jogadores = list()


while True:
  
    golsjogo = 0
    
    cadastro = dict()
    campeonato = list()
    
    print('-='*10,'CADASTRO DE JOGADORES','-='*10)
    
    cadastro['nome'] = str(input('Nome do jogador: '))
    cadastro['partidas'] = int(input('Quantas partidas jogou: '))
    
    if cadastro['partidas'] > 0:
        for p in range (1,cadastro['partidas']+1):
            gol = int(input(f'Quantos gols o jogagodr {cadastro['nome']} fez na {p}º partida: '))
            campeonato.append(gol)
            golsjogo += gol
    
    
    cadastro['gols'] = campeonato[:]
    cadastro['totalgols'] = golsjogo
    jogadores.append(cadastro.copy())
    
    campeonato.clear()
    
    
    
    resp = str(input(('Deseja continuar: [S/N]'))).upper().strip()[0]
        
    if resp not in 'SN':
        resp = str(input('Opção inválida digite apenas S ou N:'))
    if resp =='N':
        break
    
print('-'*40)
print(f'{"cod":<4}{"nome":<15}{"gols":<20}{"total":<5}')
print('-'*40)
for k , v in enumerate(jogadores):
    print(f'{k:<4}{v["nome"]:<15}{str(v["gols"]):<20}{v["totalgols"]:<5}', end='')
    print()
print('-'*40)        

while True:
    busca = int(input('Digte o codigo do jogador que deseja buscar [999 para parar]: '))
     
    if busca == 999:
        break
    
    if busca >= len(jogadores):
        print(f'ERRO! o jogador com o codigo {busca} não existe')
    else:
        print(f'Levantamento do jogador {jogadores[busca]["nome"]}:')
        for k, v in enumerate(jogadores[busca]["gols"]):
            print(f' No jogo {k+1} fez {v} gols.')
    print('-'*40)
print('<<VOLTE SEMPRE>>')