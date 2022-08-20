nombre = input('\nHola, cual es tu nombre? ')

menu = int(input(f"""\n
Bienvenido {nombre} al conversor de pesos a dolares (USD)

                    1.-Pesos Mexicanos
                    2.-Pesos Argentinos
                    3.-Pesos Colombianos
                    4.-Sorpresa

Elige una opcion: """))

if menu == 1:
    pesos = int(input(f'\n{nombre.capitalize()} cuantos pesos mexicanos tienes? '))
    value = 19.85
    dolares = pesos / value 
    print(f'\n{nombre.capitalize()} tienes ${str(round(dolares, 2))} dolares')
elif menu == 2:
    pesos = int(input(f'\n{nombre.capitalize()} cuantos pesos mexicanos tienes? '))
    value = 183.93
    dolares = pesos / value 
    print(f'\n{nombre.capitalize()} tienes ${str(round(dolares, 2))} dolares')
elif menu == 3:
    pesos = int(input(f'\n{nombre.capitalize()} cuantos pesos colombianos tienes? '))
    value = 4876.93
    dolares = pesos / value 
    print(f'\n{nombre.capitalize()} tienes ${str(round(dolares, 2))} dolares')
elif menu == 4:
    for i in range(1, 50):
        print('\n')
else:
    print('\n')
    for i in range(1, 25):
        print(f'{i}: {nombre.capitalize()} ingresa un valor correcto.')
    print('\n')
