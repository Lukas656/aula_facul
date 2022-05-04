vcompra = float(input('Digite o vlaor da compra: '))

if vcompra > 200:
    total = vcompra * 0.20

else:
    total = vcompra

print(f'O Valor da sua compra é de: R$ {total:.2f}')