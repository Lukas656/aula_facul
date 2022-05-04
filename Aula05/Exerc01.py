idade = float(input('Digite sua idade: '))


if idade < 16:
    print('Situação: Não-eleitor')
elif idade == 17:
    print('Situação: Eleitor facultativo')
elif idade >= 65:
    print('Situação: Eleitor facultativo')
else:
    print("Situação: Elitor Obrigatório")