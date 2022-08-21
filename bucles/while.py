def run():
    menu = f"""\
Bienvenido a este script de tablas de multiplicar

1.Tabla Unica
2.Tablas Infinitas

Elige una opcion: """

    bienvenida = '\nBienvenido al modo de tablas infinitas'
    menu_inf = f"""\n
Para salir del menu de Tablas Infinitas ingresa: 0
Ingresa un numero positivo: """
    opcion = int(input(menu))
    if opcion == 1:
        numero = int(input('\nIngresa un numero positivo: '))
        if numero > 0:
            print(f'\nTABLA DEL {numero}')
            for i in range(1, 11):
                print(f'{numero} x {i} es = {numero*i}')
        else:
            comprobar = True
            while comprobar == True:
                print('\nIngresaste un numero negativo.')
                n = int(input('Tienes otra oportunidad, ingresa un numero positivo: '))
                if n > 0:
                    print(f'\nTABLA DEL {n}')
                    for i in range(1, 11):
                        print(f'{n} x {i} es = {n*i}')
                    comprobar = False
    elif opcion == 2:
        print(bienvenida)
        comprobar = True
        while comprobar == True:
            num = int(input(menu_inf))
            if num > 0:
                print(f'\nTABLA DEL {num}')
                for i in range(1, 11):
                    print(f'{num} x {i} es = {num*i}')
            elif num == 0:
                print('\nAcabas de usar este script')
                break
            else:
                print()

if __name__ == '__main__':
    run()