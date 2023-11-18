#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

f = int(input('Quantos graus fahrenheit? '))
c = 5 * ((f-32) /9)

print(f'{f} graus fahrenheit são {c:.2f} graus celsius')