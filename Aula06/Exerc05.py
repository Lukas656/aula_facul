#qtd de latas é area * 3 / latas = math.ceil(area*3)
# math.ceil() arredonda para cima
import math
area = int(input('Digite a área a ser pintada (em m²): '))

qtinta = area/3
latas = math.ceil(qtinta/18)

total = latas * 80

print(f'Você precisará comprar {latas} latas')
print(f'O valor total a ser pago será de R$ {total:.2f}')