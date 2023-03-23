listas = input('crie sua lista: ') 

listas = list(map(int, listas.split()))

numero_do_usuario = int(input('Esolha um numero da sua lista para dividir: '))

numeros_divisiveis = []

for numero in listas:
    if numero % numero_do_usuario == 0:
        numeros_divisiveis.append(numero)
        
print(f'Os números divisíveis por {numero_do_usuario} são: ', numeros_divisiveis)