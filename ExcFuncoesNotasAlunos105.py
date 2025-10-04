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

while True:
    aluno = dict() # turma = {}
    aluno['nome'] = input('Nome do aluno: ').strip()
    notas_aluno = []
    
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
for aluno in turma:
    if mostra_sit == 'S':
        resultado = notas(*aluno['notas'], sit=True)
    else:
        resultado = notas(*aluno['notas'])
    print(f"Aluno: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Resumo: {resultado}")
    print('-'*30)