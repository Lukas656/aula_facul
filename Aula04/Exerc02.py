turno = input('Digite o turno periodo em que trabalha (N/D): ')
horas = float(input('Digite a quantidade de horas trabalhadas: '))

if turno == 'N':
    salario = horas * 45
    print(f'seu salário é de R$ {salario:.2f}')

else:
    salario = horas * 37.50
    print(f'Seu Salário é de R$ {salario:.2f}')


