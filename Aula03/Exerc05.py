import math

graus = float(input('Digite Um valor em graus: '))

radiano = math.radians(graus)
seno = math.sin(graus)
cosseno = math.cos(graus)
tangente = math.tan(graus)

print(f'Radiano: {radiano:.2f}')
print(f'Seno: {seno:.2f}')
print(f'Cosseno: {cosseno:.2f}')
print(f'Tangente: {tangente:.2f}')