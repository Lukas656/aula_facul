soma = 0
qtr = 0
qtb = 0
for i in range(10):
    idade = int(input('Digite sua Idade:'))
    op = int(input('Digite Sua opinião sobre o Filme: \n[1]Exelente \n[2]bom \n[3]regular\n'))
    while str(op) not in '123': #loop de consistencia, ele obriga digitar somente os numeros declarados
        print('Opção inválida!!')
        op = int(input('Digite Sua opinião sobre o Filme: \n[1]Exelente \n[2]bom \n[3]regular\n'))
    soma += idade
    if idade >= 40 and op == 3: qtr +=1
    elif op == 2: qtb += 1
media = soma / 10
    
print(f'Média das idades: {media:.2f} anos')
print(f'Quantidade de pessoas maiores de 40 anos que responderam Regular: {qtr}')
print(f'Quantidade de pessoas maiores de 40 anos que responderam Bom: {qtb}')
print(f'')    