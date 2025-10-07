##Exercício Python 105: 
# Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# TOTAL DE NOTAS
# MAIOR NOTA
# MENOR NOTA
# MEDIA DA TURMA


def notas(*notas, sit=False):
    """
    -> Calcula estatísticas de notas de alunos.
    :param notas: lista de notas do aluno
    :param sit: valor opcional, indica se deve mostrar a situação
    :return: dicionário com as informações
    """
    resultado = dict()
    resultado['total'] = len(notas)
    resultado['maior'] = max(notas)
    resultado['menor'] = min(notas)
    resultado['media'] = sum(notas) / len(notas)
    
    if sit:
        if resultado['media'] < 6:
            resultado['situação'] = 'RUIM'
        else:
            resultado['situação'] = 'BOM'
    
    return resultado
    
# Programa principal
print('-'*15, 'CADASTRO DE ALUNOS', '-'*15)

turma = list()   # turma = []

# while que cadastra uma turma de alunos cada aluno com varias notas
while True:
    aluno = dict() # aluno = {}
    aluno['nome'] = input('Nome do aluno: ').strip()
    notas_aluno = list()
    # WHILE QUE DIGITA QUANTAS NOTAS QUISER    
    while True:
        nota = input('Digite uma nota do aluno (ou ENTER para parar): ').strip()
        if nota == '':
            break
        notas_aluno.append(float(nota))
    
    aluno['notas'] = notas_aluno
    turma.append(aluno)
    continuar = input('Deseja cadastrar outro aluno? [S/N]: ').upper().strip()[0]
    
    if continuar == 'N':
        break

mostra_sit = input('Deseja mostrar a situação dos alunos? [S/N]: ').upper().strip()[0]
while mostra_sit not in 'SN':
    mostra_sit = input('Digite apenas S ou N: ').upper().strip()[0]

print('-'*30)

# um for que chama a função notas e verifca se vai ver ou não a situação da turma
for aluno in turma:
    
    if mostra_sit == 'S':
        resultado = notas(*aluno['notas'], sit=True)
    else:
        resultado = notas(*aluno['notas'])
    
    print(f"Aluno: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Resumo: {resultado}")
    print('-'*30)

# Mostrar dados da turma 

soma_nota = quantidade_notas = 0

for aluno in turma:
    soma_nota += sum(aluno['notas'])
    quantidade_notas += len(aluno['notas'])

print('-'*30)
print(f'Soma total das notas da turma: {soma_nota}')
print('-'*30)

print(f'Quantidade de Notas da turma: {quantidade_notas}')
print('-'*30)

print(f'Quantidade de Alunos da turma {len(aluno)}')
print('-'*30)
if quantidade_notas > 0:
    print(f'Média geral da Turma: {soma_nota /quantidade_notas:.2f}')
    print('-'*30)
else:
    print('nenhuma nota cadastrada')
    print('-'*30)