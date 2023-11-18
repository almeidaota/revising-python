#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

periodo = str(input("Digite o período que estuda: Matutino, Vespertino ou Noturno [M/V/N]"))

if periodo in "Nn":
    print("Boa noite")

elif periodo in "Mm":
    print("Bom dia")

elif periodo in "Vv":
    print("Boa tarde")

else:
    print("Valor inválido.")