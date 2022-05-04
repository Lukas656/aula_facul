inicial = input('Digite a Temperatura inicial em °C: ')
final = input('Digite a Temperatura final em °C: ')

variacaoC = final - inicial
variacaoF = variacaoC * 1.8 

print(f'Variação de temperatura em °C: {variacaoC:.2f} °C')
print(f'Variação de temperatura em °F: {variacaoF:.2f} °F')