listas = input('crie sua lista: ') #pedindo para o usuario criar a lista

listas = list(map(int, listas.split()))

repetidos = []
unicos = set()

for numero in listas:
    if numero not in unicos:
        unicos.add(numero)
    else:
        repetidos.append(numero)
        
repetidos = list(set(repetidos))

print('Os números que se repetem são: ', repetidos)