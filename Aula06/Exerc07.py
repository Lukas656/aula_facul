print('Coordenadas de um pont P(x, y)')
x = float(input('Digite a coordenada X: '))
y = float(input('Digite a coordenada Y: '))

if x > 0 and y > 0 :
    print(f'O ponto p({x}, {y}) pertence ao 1º Quadrante')

elif x < 0 and y > 0 :
    print(f'O ponto p({x}, {y}) pertence ao 2º Quadrante')

elif x < 0 and y < 0 :
    print(f'O ponto p({x}, {y}) pertence ao 3º Quadrante')

elif x > 0 and y < 0 :
    print(f'O ponto p({x}, {y}) pertence ao 4º Quadrante')

else:
    print('Coordenadas inválidas')