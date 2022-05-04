carneirinnhos = 0

while True:
    sono = input('Já Durmiu s/n ? ')
    if sono in 'nN':
        carneirinnhos += 1
    else: break


print(f'Você contou {carneirinnhos} carneirinhos')