#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

list = []
s = 0

for i in range (0, 4): 
    n = float(input('Digite a nota do bimestre: '))
    s += n
    list.append(n)


media = s/ len(list)

print('As notas individuais foram: ', end = '')
for i in list:
    print (i, end = ', ')

print(f'\nA média do bimestre é: {media}')