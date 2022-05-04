nome = input('Qual o seu nome? ')
horas = float(input('Que horas são [0 - 23]? '))

if horas > 5 and horas < 12:
    print(f'Bom dia {nome}')

elif horas > 13 and horas < 18:
    print(f'Boa Tarde {nome}')

elif horas > 19 :
    print(f'Boa Noite {nome}')

elif  horas < 4 :
    print(f'Boa Noite {nome}')

else:
    print(f'Algo de errado não está certo {nome}')