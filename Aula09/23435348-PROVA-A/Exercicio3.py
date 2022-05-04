sbruto = float(input('Digite o salário bruto R$: '))

if sbruto < 1000:
    sliquido = sbruto + 200
        
elif sbruto < 1250:
    sliquido = sbruto + 150
    
elif sbruto < 1750:
    
    sliquido = sbruto + 100
else:
    sliquido = sbruto + 75
    
sliquido = sliquido * 1.11
    
print(f'Valor do salario é {sliquido:.2f}')
 
    
    