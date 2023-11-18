#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

n1 = int(input('Digite o preço do primeiro produto: '))
n2 = int(input('Digite o preço do segundo produto: '))
n3 = int(input('Digite o preço do terceiro produto: '))

if n1 < n2 and n1 < n3:
    print('O primeiro produto é o melhor.')
elif n2 < n1 and n2 < n3:
    print('O segundo produto é o melhor.')
else:
    print('O terceiro produto é o melhor.')