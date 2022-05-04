nome = input('Digite o Nome do produto: ')
venda = float(input('Digite o valor da venda: '))

if venda < 10:
    lucro = venda * 1.70

elif venda < 30:
    lucro = venda * 1.50

elif venda <50:
    lucro = venda * 1.40

elif venda >= 50:
    lucro = venda * 1.30

print(f"nome: {nome} Total: {lucro:.2f}")