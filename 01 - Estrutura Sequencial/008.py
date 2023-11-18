#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hora = float(input('Qual o valor da sua hora?'))
mes = float(input('Quantas horas trabalhou esse mês?'))

sal = hora * mes

print(f'Seu salário será de R${sal:.2f} nesse mês')