# formula = dis = (Idade * 365) + (meses * 30) + dias vividos no mes atual

anos= int(input('Quantos anos você tem ?: '))
meses = int(input('Numero do mês atual ?: '))
dias = int(input('digite a quantidade de dias do mês ?: '))


idadeexpressa = anos * 365 + meses * 30 + dias

print(f'Voce tem {idadeexpressa} dias de vida ')