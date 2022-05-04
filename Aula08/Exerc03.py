eleitores = 0
maiores = 0
nelelitores = 0

for idade in range(500):
    idade = int(input('Digite a idade do aluno: '))
    if  idade >= 16:
        eleitores += 1
    else:
        maiores += idade
        nelelitores += 1
        
media = maiores / nelelitores
print(f'A quantidade de eleitores é {eleitores}')
print(f'A media dos não-eleitores é {media}')