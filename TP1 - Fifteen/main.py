import logica

# Se puede modificar el tamaño del tab junto con sus controles
TAMANIO = (4, 4)
CONTROLES = ("w", "a", "s", "d", 'o')


def main():
    """DOC: Contiene el codigo de control del juego"""
    tablero = logica.inicializar_tablero(TAMANIO)
    logica.mover_ficha_random(tablero, CONTROLES)
    movimientos_totales = 0

    while True:
        print()
        logica.mostrar_tablero(tablero)
        print(f'Controles: {CONTROLES[:-1]}')
        print(f"Salir del juego: '{CONTROLES[-1]}'")
        print(f'Movimientos realizados: {movimientos_totales}')

        while True:
            direccion = list(input("Entrada: "))

            if logica.validar_input(direccion, CONTROLES):
                for movimiento in direccion:
                    if movimiento == CONTROLES[-1]:
                        return

                    if movimiento in CONTROLES:
                        tablero = logica.mover_ficha(
                            tablero, movimiento, CONTROLES)
                        movimientos_totales += 1

                    if logica.gano(tablero):
                        logica.mostrar_tablero(tablero)
                        print('Ganaste! :)')
                        return

                    if movimientos_totales >= 10 * (len(tablero) * len(tablero[0])):
                        logica.mostrar_tablero(tablero)
                        print('Perdiste! :(')
                        return
                break
            print()
            print(f"Ingrese solo movimientos del tipo {CONTROLES}.")
            break


main()
