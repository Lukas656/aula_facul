while True:
    print('_' * 30)
    print('Calculadora da base 10 (decimal) ')
    print('_' * 20)
    print('[1] Binario para Decimal')
    print('[2] Octal para Decimal')
    print('[3] Hexadecimal para Decimal')
    print('[0] sair')
    opcao = int(input('Digite uma opção: '))
    if opcao == 0:
        break
    elif opcao ==1:
        bin = input('Digite o número binario: ')
        dec = int(str(bin),2)
        print(f'O numero bin {bin} equivale a {dec} em Decimal')

    elif opcao ==2:
       x = int(input('Digite o número Octal: '))
       dec = 0
       remain = x 
       i = 0
       while remain > 0:
          dec += int(remain % 10) * 8 ** i 
          remain = int(remain/10)
          i += 1
       print(f'O numero octal {x} digitado vale {dec} em decimal')

    elif opcao ==3:
     cont = input('Digite o número hexa: ')
     dec = int(cont, 16)

     print(f'O numero Hexa ({cont}) digitado vale {dec} em decimal')

    else:
      print('Opção invalida')