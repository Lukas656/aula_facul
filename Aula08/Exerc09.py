maior = 0
nomedele = 0
for n in range(10):
    nome =input('Digite o Nome: ')
    altura= float(input(f'Digite a aultura do(a) aluno(a) {nome} em cm: '))
    
    if n == 1:
        nomedele = nome
        maior = altura
n += n
print(f'O maior é {nomedele} com {maior}')
