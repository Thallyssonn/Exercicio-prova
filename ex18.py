listas = input('crie sua lista: ') 

listas = list(map(int, listas.split()))

lista_com_numeros_divisiveis_por_3 = []

for numero in listas:
    if numero % 3 == 0:
        lista_com_numeros_divisiveis_por_3.append(numero)
        
print('Os números que são divisíveis por 3: ', lista_com_numeros_divisiveis_por_3)