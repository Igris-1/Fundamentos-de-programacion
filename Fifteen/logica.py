import random


def inicializar_tablero(TAMANIO):
    """DOC: Inicializa un tablero de tamaño 'TAMANIO'x'TAMANIO'"""
    tablero = []
    for fila in range(TAMANIO[1]):
        tablero.append([])
        for columna in range(TAMANIO[0]):
            tablero[fila].append(fila * TAMANIO[0] + columna + 1)
    tablero[-1][-1] = 0
    return tablero


def mostrar_tablero(tablero):
    """DOC: Muestra el tablero en consola"""
    largo = 0
    for fila in tablero:
        for num in fila:
            if num > largo:
                largo = num
    espacios = len(str(largo))

    if len(tablero) > 4:
        print("=== ¿Fifteen? ===")
    else:
        print("=== Fifteen ===")

    for fila in range(len(tablero)):
        fila_actual = "|"
        for numero in tablero[fila]:
            if numero == 0:
                fila_actual += " " * espacios + "|"
            else:
                fila_actual += " " * \
                    (espacios - len(str(numero))) + str(numero) + "|"
        print(fila_actual)


def mover_ficha_random(tablero, CONTROLES):
    """DOC: Genera las posiciones iniciales de las fichas"""
    for _ in range((len(tablero) * len(tablero[0])) * 2):
        direccion = random.choice(CONTROLES[:-1])
        mover_ficha(tablero, direccion, CONTROLES)


def mover_ficha(tablero, direccion, CONTROLES):
    """DOC: Mueve la ficha en la dirección indicada"""
    mas_menos_fila = 0
    mas_menos_columna = 0

    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if tablero[fila][columna] == 0:

                if direccion == CONTROLES[2]:
                    if fila > 0:
                        mas_menos_fila = -1
                        mas_menos_columna = 0
                        return movimiento(tablero, fila, columna, mas_menos_fila, mas_menos_columna)

                elif direccion == CONTROLES[0]:
                    if fila < len(tablero) - 1:
                        mas_menos_fila = 1
                        mas_menos_columna = 0
                        return movimiento(tablero, fila, columna, mas_menos_fila, mas_menos_columna)

                elif direccion == CONTROLES[3]:
                    if columna > 0:
                        mas_menos_fila = 0
                        mas_menos_columna = -1
                        return movimiento(tablero, fila, columna, mas_menos_fila, mas_menos_columna)

                elif direccion == CONTROLES[1]:
                    if columna < len(tablero[fila]) - 1:
                        mas_menos_fila = 0
                        mas_menos_columna = 1
                        return movimiento(tablero, fila, columna, mas_menos_fila, mas_menos_columna)
    return tablero


def movimiento(tablero, fila, columna, mas_menos_fil, mas_menos_col):
    """DOC: Intercambia la ficha con la ficha de la posición indicada"""
    tablero[fila][columna], tablero[fila + mas_menos_fil][columna +
    mas_menos_col] = tablero[fila + mas_menos_fil][columna + mas_menos_col], tablero[fila][columna]
    return tablero


def validar_input(direccion, CONTROLES):
    """DOC: Valida que el input sea una dirección válida"""
    for movimiento in direccion:
        if movimiento not in CONTROLES:
            return False
    return True


def gano(tablero):
    """DOC: Valida si el jugador ganó"""
    unica_fila = []
    for fila in tablero:
        unica_fila += fila


    fila_ordenada = sorted(unica_fila)

    for i in range(len(fila_ordenada) - 1):
        fila_ordenada[i], fila_ordenada[i - 1] = fila_ordenada[i - 1], fila_ordenada[i]
    return fila_ordenada == unica_fila
