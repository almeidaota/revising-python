#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.


import math

raio = float(input('Digite o raio do círculo: '))
area = math.pi * (raio ** 2)
print(f'a área do cirulo é {area:.2f}')
