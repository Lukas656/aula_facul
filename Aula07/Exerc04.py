positivo = 0
negativo = 0
menor = 0

while True:
    num = float(input('Digite um numero real (0 sair): '))
    if menor == 0:
        menor = num
    elif num < menor:
        menor = num
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
    else: break
    
print(f'menor numero digitado {menor}')
print(f'numeros positivos {positivo}')
print(f'numeros negativos {negativo}')