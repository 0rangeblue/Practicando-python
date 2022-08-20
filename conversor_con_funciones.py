def converter(pais, value):
    pesos = int(input(f"""\n
{nombre.capitalize()} introduce la cantidad de pesos {
    pais.capitalize()
} que vas a convertir: """))
    dolares = pesos / value 
    print(f"""\n
{nombre.capitalize()} tienes ${str(
    round(dolares, 2)
)} dolares""")

nombre = input('\nHola, cual es tu nombre? ')

menu = f"""\n
Bienvenido {nombre} al conversor de monedas latinoamericanas a dolares

            1.-Pesos Mexicanos
            2.-Pesos Argentinos
            3.-Pesos Colombianos

Elige una opcion: """

option = int(input(menu))

if option == 1:
    converter('mexicanos', 19.84)
elif option == 2:
    converter('argentinos', 164.45)
elif option == 3:
    converter('colombianos', 4258.53)
else:
    for i in range(1, 584):
        print(f'{i}: {nombre.capitalize()} introduce un valor correcto.')
        i += 1