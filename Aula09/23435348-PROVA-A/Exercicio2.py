# digitar o raio e receber o comprimento e volume
# Comprimento: C = 2*pi*raio
# volume: V = 4/3 * pi * raio³


import math

raio = float(input('Digite o raio da esfera em cm: '))

comprimento = 2 * math.pi * raio
volume = 4/3 * math.pi * raio**3

print(f'Comprimento da circunferência da esfera: {comprimento:.2f} cm²')
print(f'Volume da esfera: {volume:.2f} cm³')