#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

c = int(input('Quantos graus celsius? '))
f = c * (9/5) + 32


print(f'{c} graus celsius são {f:.2f} graus fahrenheit') 