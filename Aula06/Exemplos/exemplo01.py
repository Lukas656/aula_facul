valor = float(input('digite o Valor da Compra: '))
parcelas = int(input('digite o Valor das Parcelas: '))

match(parcelas):
    case 2:valor = valor * 1.03
    case 4:valor = valor * 1.07
    case 6:valor = valor * 1.09
    case 8:valor = valor * 1.12  
    case _: valor  = 0 #Caso nenhuma das opções foi solucionada.

if valor == 0:
    print('opção invalida')
else:
    print(f'O Valor da parcela é R${valor/parcelas}')