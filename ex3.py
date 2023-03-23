#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, encontre o número máximo e o número mínimo da lista.
print('Digite uma lista de numeros')

lista = []

for i in range(5):
    lista.append(int(input('Digite um numero: ')))

minimo = min(lista)
maximo = max(lista)

print('numero maximo',minimo)
print('numero minimo',maximo)