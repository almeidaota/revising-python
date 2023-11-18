#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps)
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).


from math import ceil

tam_arquivo = int(input('Qual o tamanho do arquivo? [MB]'))
vel_internet = int(input('Qual a velocidade da internet? [Mbps] '))

#transformando megabytes em megabits
tam_arquivo *= 8

tempo = (tam_arquivo / vel_internet) / 60

print(f'O tempo necessário para realizar o download será de {ceil(tempo)} minutos. ')

