#Verificar se o numero é positivo

numero = int(input('Digite um número inteiro: '))

if numero > 0:
    print(f'O Número {numero} é Positivo')
elif numero == 0:
    print(f'O Numero {numero} é Nulo')
else:
    print(f'O Numero {numero} é Negativo')