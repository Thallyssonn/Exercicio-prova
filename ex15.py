#Escreva um programa que peça ao usuário para digitar uma lista de números e, em seguida, crie uma nova lista que contenha apenas os números que aparecem mais de uma vez na lista original.
listas = input('crie sua lista: ') 
listas = list(map(int, listas.split()))


lista_com_duplicatas = listas

lista_sem_duplicatas = []
for i in range(5):

while lista_com_duplicatas:
    elemento = lista_com_duplicatas.pop(0) 
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento) 
        

print('A lista sem duplicatas é:', lista_sem_duplicatas)