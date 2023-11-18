#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sex = str(input('Qual seu sexo? [Ḿ/F] '))

if sex in 'Ff':
    print('Sexo Feminino')

elif sex in 'Mm':
    print('Sexo masculino')

else:
    print('Sexo Inválido')