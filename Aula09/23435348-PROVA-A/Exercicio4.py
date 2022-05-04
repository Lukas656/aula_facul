n = int(input('Digite a Quantidade de Alunos: '))
ap = 0
soma = 0
af = 0
for i in range(n):
    media = float(input(f'Digite a Média do {i+1}º aluno: '))
    soma += media
    if media >= 6.0: ap += 1
    elif media >= 1: af += 1

mediaT = soma / n    
    
print(f'Quantidade de Alunos aprovados: {ap} alunos.')
print(f'A media Geral da Turma: {mediaT:.2f}')
print(f'Quantidade de alunos de avaliação final: {af} alunos.')