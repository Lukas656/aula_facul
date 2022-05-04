n1 = float(input('Digite o Primeiro Número: '))
n2 = float(input('Digite o Segundo Número: '))
print('[1] Média')
print('[2] Diferença maior-menor')
print('[3] produto')
print('[4] Divisão n1/n2')

opcao = int(input('Digite uma Opção: '))
if opcao < 1 or opcao > 4:
    print('Opção invalida!')
elif opcao == 4 and n2 == 0:
    print('Inpossivel dividir por Zero!')

else:
    if opcao == 1:
        media = (n1 + n2) /2
        print(f'Média = {media}')
    elif opcao == 2:
        diferenca = n2 - n1
        print(f'Diferença = {diferenca}')
    elif opcao == 3:
        produto = n1 * n2
        print(f'Produto = {produto}')
    elif opcao == 4:
        divisao = n1 / n2
        print(f'Divisão = {divisao}')
    else:
        print('Algo de errado não está certo')
