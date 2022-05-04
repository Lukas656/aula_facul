valor_hora = float(input('Digit o valor da hora aula: R$'))
carga_horaria = int(input('Digite a carga horária semanal: '))

salario_base = valor_hora * carga_horaria * 4.5
adicional = salario_base * 1/6

salario_final = salario_base + adicional

print(f'Salario Final: R$ {salario_final}')