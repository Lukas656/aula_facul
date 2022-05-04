nota1 = float(input('Digite a primeira nota parcial: '))
nota2 = float(input('Digite a segunda nota parcial: '))

media = (nota1 + nota2)/2

if media >= 9.0:
    print('conceito: A')
    print('menssagem: Aprovado')
    
elif media >= 7.5:
    print('conceito: B')
    print('menssagem: Aprovado')
    
elif media >= 6.0:
    print('conceito: C')
    print('menssagem: Aprovado')
    
elif media >= 4.0:
    print('Conceito: D')
    print('menssagem: Reprovado')
    
else:
    print('Conceito: E')
    print('menssagem: Reprovado')