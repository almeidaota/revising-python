#   Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#    Para homens: (72.7*h) - 58
#   Para mulheres: (62.1*h) - 44.7

h = float(input('Digite sua altura: '))
s = str(input('Digite seu sexo [M/F] ')).lower()

if s in "m":
    peso_ideal = (72.7*h) - 58
    print(f'O peso ideal de um homem dessa altura é de {peso_ideal} kgs')
elif s in "f":
    peso_ideal = (62.1*h) - 44.7
    print(f'O peso ideal de uma mulher dessa altura é de {peso_ideal} kgs')


else:
    print('Digite um sexo válido. Programa encerrado')