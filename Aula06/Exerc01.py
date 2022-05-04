#Entrada de dados
salario = float(input('Digite o Salário Fixo: '))
vendas = float(input('Digite o valor das vendas: '))

#processamento
comissao = vendas * 0.04
salario += comissao

#saida
print(f'Comissão: {comissao:.2f}') 
print(f'Salário Final:{salario:.2f} ') 