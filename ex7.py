#Escreva um programa que peça ao usuário para digitar uma lista de nomes e, em seguida, imprima o nome mais longo e o nome mais curto da lista.
print('Digite uma lista numeros\n')

lista = []
total = []
n=0
for i in range(5):
    lista.append(str(input("Digite um nome: ")))

for x in lista:
    total.append(len(lista[n]))
    n+=1


for u in lista: 
    if min(total) == len(u):
        print('menor nome', ':', u)
    if max(total) == len(u):
        print('maior nome', ':', u)