valorprestacao = float(input('Digite o valor da prestação: '))
multa = float(input('Digite a porcentagem de multa pelo atraso: '))
qtdeDias = float(input('Digite a quantidade de dias de atraso: '))

prestacao = valorprestacao+(valorprestacao*(multa/100)*qtdeDias)

print(f'Sua prestação está no valor de R$ {prestacao:.2f}')