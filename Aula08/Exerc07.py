cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
while True:
    num = int(input('Digite um numero positivo (-1 para sair): '))
    
    if num < 0:
        break
    if num >=0 and num <= 25:
        cont1 += 1
    elif num  <= 50:
        cont2 += 1
    elif num  <= 75:
        cont3 += 1
    elif num <= 100:
        cont4 += 1
        
print(f'[0 - 25] {cont1} numeros ')
print(f'[25 - 50] {cont2} numeros')
print(f'[50 - 75] {cont3} numeros ')
print(f'[75 - 100] {cont4} numeros')