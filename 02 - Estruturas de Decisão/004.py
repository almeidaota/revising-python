#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.


letter = str(input('digite uma letra'))

if letter in 'AaEeIiOoUu':
    print('Vogal')
    
else:
    print('Consoante')