# Lucas Santos nascimento
# 23435348
# Prova_A


#coversao = dolar*cotacao

item1 = float(input('Digite o valor do primeiro item em dólares Us: '))
item2 = float(input('Digite o valor do segundo item em dólares Us: '))
cotacao = float(input('Digite a cotação do dólar hoje: R$  '))
 
conversao = (item1 + item2)*cotacao

print(f'Valor a ser pago em reais: R$ {conversao:.2f}')