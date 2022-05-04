import math
a =float(input('Digite o Coef A: '))
b = float(input('Digite o Coef B: '))
c = float(input('Digite o Coef C: '))

if a == 0:
    print('Não é equação de 2° grau!')

else:
    delta = b**2 - 4 *a *c
    if delta < 0:
        print('Não Há Raiz')
        
    elif delta == 0:
        x = (-b + math.sqrt(delta))/2*a
        print(f'X1 = X2 = {x}')
    
    else:
        x1 = (- b + math.sqrt(delta))/2 *a 
        x2 = (- b - math.sqrt(delta))/2 *a
        print(f'X1 = {x1:.2f} e X2 = {x2:.2f}') 

