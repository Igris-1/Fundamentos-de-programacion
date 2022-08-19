import gamelib

def inicializar_tablero(TAMANIO):
    """DOC: Genera la matriz inicial"""
    return [['' for _ in range(TAMANIO)] for _ in range(TAMANIO)]

def mapeo_de_pixeles(x, y):
    """DOC: Convertir coordenadas de pixeles a posiciones"""
    return int(x/25), int(y/25)

def celda_vacia(tablero, x, y):
    '''DOC: Devuelve un tipo de dato bool si la celda esta vacia'''
    fila, columna = mapeo_de_pixeles(x, y)

    if y < len(tablero) * 25 and x < len(tablero) * 25:
        celda_vacia = tablero[fila][columna] == ''
        return celda_vacia

def centro_de_celda(fila, columna):
    """DOC: Devuelve las coordenadas del centro de la celda"""
    mitad_celda_f = 12.5 + 25 * fila
    mitad_celda_c = 12.5 + 25 * columna
    return mitad_celda_f, mitad_celda_c

def juego_actualizar(tablero, x, y, turno):
    """  
    DOC: Actualizar el estado del juego
         x e y son las coordenadas (en pixels) donde el usuario hizo click.
         Esta función determina si esas coordenadas corresponden a una celda
         del tablero; en ese caso determina el nuevo estado del juego y lo
         devuelve.
    """
    fila, columna = mapeo_de_pixeles(x, y)
    vacio = celda_vacia(tablero, x, y)

    if vacio:
        if turno == 0:
            tablero[fila][columna] = 'O'
            turno = 1
        else:
            tablero[fila][columna] = 'X'
            turno = 0
    return tablero, turno

def turnos(turno):
    if turno == 1:
        return "Turno de X"
    return "Turno de O"

def juego_mostrar(tablero, turno, TAMANIO):
    """DOC: Actualizar la ventana"""
    mostrar_tablero(tablero)
    turno = turnos(turno)
    gamelib.draw_text(turno, 25 * (TAMANIO) / 2, 25 * (TAMANIO) + 11, fill='white', size=15)

    if TAMANIO > 10:
        gamelib.draw_text('5 en linea?', 30, 25 * (TAMANIO) + 11, fill='white', size=8)

    for i in range(len(tablero)):
        for j in range(len(tablero)):
            centro_celda_f, centro_celda_c = centro_de_celda(i, j)
            gamelib.draw_text(tablero[i][j], centro_celda_f, centro_celda_c, fill='white', anchor='c')

def mostrar_tablero(tablero):
    for fila in range(len(tablero)):
        for columna in range(len(tablero)):
            gamelib.draw_rectangle(fila * 25, columna * 25, fila * 25 + 25, columna * 25 + 25, outline='white', fill=None)