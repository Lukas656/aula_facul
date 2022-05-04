mb = float(input('Digite o tamanho do arquivo em MB: '))
velocidade = float(input('Digite a  velocidade do link da internet (Mbps): '))

tempo = mb/velocidade
min = tempo // 60
seg = tempo % 60

print(f'Tempo aproximado para download: {min} e segundos {seg} ')