import math
soma = 0
n = int(input('Digite a qtde de Turmas: '))

for i in range(n):
    alunos = input(f'Digite a qtde de alunos da {i+1}° turma: ')
    soma += alunos
media = math.ceil(soma/n)  

print(f' As turmas tem em media {media} alunos.')