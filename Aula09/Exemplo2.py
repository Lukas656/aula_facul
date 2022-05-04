#imprime o inverso do digitado.

nome = input('Digite uma string qualquer: ')
inv = ''
for d in nome:
   inv = d + inv    
print(inv)

# Ou Mais simples ainda..

nome2 = input('Digite qualquer string: ')
print(nome2[::-1])