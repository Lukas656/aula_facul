import math
h =  float(input('Digite a altura do tronco da piramede: '))
bmenor = float(input('Digite a base menor do tronco da piramede: '))
bmaior = float(input('Digite a base maior do tronco da piramede: '))

bmaior = bmaior**2
bmenor = bmenor**2
h = h
volume = h/3*(bmenor+ math.sqrt(bmaior*bmenor)+bmaior)

print(f'O Volume do tronco é: {volume} cm³')




