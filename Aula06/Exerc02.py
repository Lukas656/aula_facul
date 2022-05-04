segundos = int(input('Digite a Quantidade de Segundos: '))

horas = segundos // 3600 #Aqui eu Tiro a Hora

minutos = segundos % 3600//60 #aqui eu Retiro os minutos de horas

segundos = segundos%60 #Aqui eu retiro os Segundos de horas e minutos
 
print(f'{horas} hora , {minutos} minutos e {segundos} segundos')
