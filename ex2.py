#Escreva um programa que peça ao usuário para digitar uma lista de palavras e, em seguida, imprima apenas as palavras que começam com a letra "a
print('Digite uma lista de palavras\n')

lista  = []
newLista = []
for i in range(5):
    lista.append(str(input('digite uma palavra: ').capitalize()))

for x in lista:
    if x[0] == 'A':
        newLista.append(x)

print("palavras que comecam com a letra A: ", newLista)