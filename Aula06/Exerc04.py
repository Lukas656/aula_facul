# Calcular o Peso Ideal em relação a altura
#Entrada
altura = float(input('Digite a altura da pessoa em metros: '))
sexo = input('Digite o sexo da pessoa m/f: ')

#processamento 
if sexo == 'Mm':
    peso = (72.7 * altura) - 58
else:
    peso = (62.1*altura) - 44.7

#saida
print(f'O peso ideal dessa pessoa é: {peso:.2f}')