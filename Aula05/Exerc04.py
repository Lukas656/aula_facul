n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
operacao = input('Digite a operação que deseja (+, - , *, /): ')

if operacao == '+':
    result = n1 + n2
    print(f"{n1} {operacao} {n2} : {result}")

elif operacao == '-':
    result = n1 - n2
    print(f"{n1} {operacao} {n2} : {result}")

elif operacao == '*':
    result = n1 * n2
    print(f"{n1} {operacao} {n2} : {result}")

elif operacao == '/':
    result = n1 / n2
    print(f"{n1} {operacao} {n2} : {result}")

else:
    print('Operação invalida!')

