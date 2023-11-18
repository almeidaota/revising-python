#Faça um Programa que leia três números e mostre o maior e o menor deles.


n1 = int(input('Digite um número '))
n2 = int(input('Digite outro um número '))
n3 = int(input('Digite o último número '))

if n1 < n2 and n1 < n3:
    print(f'{n1} é menor que {n2} e {n3}')

elif n2 < n1 and n2 < n3:
    print(f'{n2} é menor que {n1} e {n3}')

else:
    print(f'{n3} é menor que {n1} e {n2}')

