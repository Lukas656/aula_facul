agua = float(input("Digite o Valor da sua conta de agua: "))
luz = float(input("Digite o Valor da sua conta de Luz: "))
net = float(input("Digite o valor da sua conta dde Internet: "))
salario = float(input("Digite seu Salário: "))

total = agua + luz + net

if salario >= total:
    resto = salario % total
    print(f'Saldo atual de: {resto:.2f}')

else:
    print('Salario insuficiente !!')