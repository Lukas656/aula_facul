texto = input('Digite um Texto: ')

pontua = ['.', ',', ';' , ':', '!' , '?']

for p in pontua:
    texto = texto.replace(p,' ') #troca por vazio/espaço em branco onde havia pontuação

texto = texto.split() # quebra onde os espaços foram declarados
print(f'Numero de palavras {len(texto)}') 