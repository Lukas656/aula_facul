soma = 0
conta = input('Digite a conta co 4 digitos: ')

for d in conta:
    soma += int(d)
    
dig = soma % 10
print(f'Número completo da conta : 00{conta}-{dig}')