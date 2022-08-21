# Apartado 1: Repasos de conceptos basicos

"""numeros = [1, 2, 3, 4, 5]
primeraPosicion = numeros[0]
longitud = len(numeros)
print(f'El primer valor es: {primeraPosicion}\nLa longitud de la lista es de: {longitud}')

for num in numeros:
    print(num)"""


# Apartado 2: Indexado y sublistas

"""lista = ['Hoy', 'hace', 'mucho', 'frio', 'en', 'la', 'ciudad']
print(lista)
ultimaPosicion = lista[-1]
print(ultimaPosicion)
penultimoElemento = lista[-2]
print(penultimoElemento)

sublista = lista[1:4]
print(sublista)
sublista = lista[:4]
print(sublista)
sublista = lista[2:]
print(sublista)

sublista = lista[-4:-1]
print(sublista)"""


# Apartado 3: Comprobar si una lista contiene o no un elemento

lista = ['Hoy', 'hace', 'mucho', 'frio', 'en', 'la', 'ciudad']
print('\n' + str(lista) + '\n')
palabra = 'ciudad'
palabraDos = 'pais'

if palabra in lista:
    print(f'La palabra: {palabra} SI pertenece a la lista')

if palabraDos not in lista:
    print('La palabra: ' + str(palabraDos) + ' NO pertenece a la lista')