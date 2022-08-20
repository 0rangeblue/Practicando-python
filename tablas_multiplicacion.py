menu = int(input(f"""\n
Bienvenido al script de tablas de multiplicar, este script tiene diferentes modos.

                    1.-Modo de tabla unica.
                    2.-Modo de tablas infinitas

Elige una opcion correcta: """))

comprobar = True 

if menu == 1:
    while comprobar == True:
        tabla = int(input('\nIntroduce un numero positivo: '))
        if tabla > 0:
            print(f'\nTABLA DEL {tabla}:')
            for i in range(1, 11):
                print(f'{i} x {tabla} es = {i * tabla}')
            comprobar = False
        else:
            print('Ingresaste un numero negativo, vuelve a intentarlo.')
elif menu == 2:
    while comprobar == True:
        num_inf = int(input(f"""\n
Ingresa 0 para salir del modo de Tablas Infinitas.
Ingresa un numero positivo para ver una tabla: """))
        if num_inf > 0:
            print(f'\nTABLA DEL {num_inf}')
            for i in range(1, 11):
                print(f'{num_inf} x {i} es = {num_inf*i}')
        elif num_inf == 0:
            comprobar = False
        else: 
            print('\nIngresa unicamente un numero positivo, vuelve a intentarlo.')
        
else:
    for i in range(1, 51):
        print(f'{i}: Ingresa unicamente numeros positivos, vuelve a intentarlo.')