masc = 0
fem = 0
contadorM = 0
contadorF = 0

while True:
    sexo = input('Digite o sexo da pessoa: ')
    altura = float(input('Digite a altura da pessoa em em m (0 para sair): '))
    if altura == 0: break
    elif sexo in 'mM':
        masc += altura
        contadorM += 1
    elif sexo in 'fF':
        fem += altura
        contadorF += 1
    else: print('Sexo Invalido')
mediaM = masc/contadorM
mediaF = fem/contadorF

print(f'Média das altura masculino: {mediaM}')
print(f'média das altura Femminino: {mediaF}')