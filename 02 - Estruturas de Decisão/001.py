#Faça um Programa que peça dois números e imprima o maior deles.


n1 = float(input('Digite um valor '))
n2 = float(input('Digite outro valor '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
else:
    print(f'{n2} é maior que {n1}')

