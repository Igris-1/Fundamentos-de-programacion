import gamelib
import random


def movimientos(ruta, tablero):
    """DOC:Lectura de archivo CSV y genera los posibles movimientos de cada pieza"""
    resultado = {}

    with open(ruta) as archivo:
        for f in archivo:
            pieza, movimiento, extension = f.rstrip().split(',')
            x, y = movimiento.split(';')
            if extension == 'true':
                for i in range(1, len(tablero)):
                    resultado[pieza] = resultado.get(
                        pieza, []) + [(int(x) * i, int(y) * i)]
            else:
                resultado[pieza] = resultado.get(
                    pieza, []) + [(int(x), int(y))]
    piezas = [pieza for pieza in resultado]
    return resultado, piezas


def inicializar_tablero(TAMANIO):
    """DOC: genera la matriz inicial"""
    return [['' for _ in range(TAMANIO)] for _ in range(TAMANIO)]


def agregar_piezas(tablero, nivel, movimientos, piezas):
    """DOC: agregado de piezas a la matriz inicial del nivel"""
    n = nivel + 1
    pieza = random.choice(piezas)
    x, y = random.randint(
        0, len(tablero) - 1), random.randint(0, len(tablero) - 1)
    tablero[x][y] = pieza
    inicial = [pieza, x, y]
    n -= 1

    while n > 0:
        x1, y1 = random.randint(
            0, len(tablero) - 1), random.randint(0, len(tablero) - 1)
        if (x1-x, y1-y) in movimientos[pieza]:
            pieza = random.choice(piezas)
            tablero[x1][y1] = pieza
            x, y = x1, y1
            n -= 1
    tablero[inicial[1]][inicial[2]] = inicial[0] + '_r'
    return inicial


def juego_mostrar(tablero, TAMANIO, nivel, inicial, movimientos):
    """DOC: dibujado de interfaz, tablero, piezas, recuadros"""
    mostrar_tablero(tablero)
    mostrar_imagenes(tablero)
    mostrar_recuadros(tablero, inicial, movimientos)

    gamelib.draw_text(f'|Nivel: {nivel}|', 30 + len(str(nivel)),
                      44 * (TAMANIO) + 14, fill='white', size=10)
    gamelib.draw_text('|Cargar Nivel: C|', 110, 44 *
                      (TAMANIO) + 14, fill='white', size=10)
    gamelib.draw_text('|Reiniciar: Z|', 200, 44 *
                      (TAMANIO) + 14, fill='white', size=10)
    gamelib.draw_text('|Salir: E|', 270, 44 * (TAMANIO) +
                      14, fill='white', size=10)


def mostrar_tablero(tablero):
    """DOC: dibujado del tablero"""
    colores = ("#2c2c44", "#191919")
    color = ''

    for columna in range(len(tablero)):
        for fila in range(len(tablero)):
            if color == 1:
                color = 0
            else:
                color = 1
            gamelib.draw_rectangle(fila * 44, columna * 44, fila * 44 + 44, columna * 44 + 44,
                                   outline='black', fill=colores[color], width=5, activedash=True, dashoffset=3)
        colores = colores[::-1]


def mostrar_imagenes(tablero):
    """DOC: dibujado de imagenes"""
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            pieza = tablero[i][j]
            if pieza:
                if pieza[-1] == 'r':
                    ruta = 'Shape-Shifter-Chess\images/' + pieza[:-1] + 'rojo.gif'
                    gamelib.draw_image(ruta, j * 44, i * 44)
                else:
                    ruta = 'Shape-Shifter-Chess\images/' + pieza + '_blanco.gif'
                    gamelib.draw_image(ruta, j * 44, i * 44)


def mostrar_recuadros(tablero, inicial, movimientos):
    """DOC: dibujado de recuadros rojos sobre las piezas"""
    pieza, x, y = inicial

    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] != '':
                if (x - i, y - j) in movimientos[pieza]:
                    gamelib.draw_rectangle(
                        j * 44, i * 44, j * 44 + 44, i * 44 + 44, outline='red', fill=None, width=2, activedash=True)


def actualizar(tablero, x, y, inicial, movimientos):
    """DOC: realiza el movimiento de la pieza correspondiente"""
    pieza, x1, y1 = inicial
    y, x = int(x / 44), int(y / 44)

    if x < len(tablero) and y < len(tablero):
        if (x, y) != (x1, y1):
            if (x - x1, y - y1) in movimientos[pieza]:
                if tablero[x][y] != '':
                    inicial = [tablero[x][y], x, y]
                    tablero[x][y] += '_r'
                    tablero[x1][y1] = ''
    return tablero, inicial


def gano(tablero):
    """DOC: verifica si el jugador gano y devuelve un tipo
     de dato bool
    """
    resultado = []

    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] != '':
                resultado.append(tablero[i][j])
    if len(resultado) > 1:
        return False
    return True


def guardar_nivel(nivel, tablero):
    """
    DOC: Guarda el ultimo nivel en un archivo CSV
    """
    piezas = {}
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] != '':
                piezas[(i, j)] = piezas.get((i, j), '') + tablero[i][j]

    with open('Shape-Shifter-Chess/ultimo_nivel.csv', 'w') as archivo:
        archivo.write(f'{nivel}\n')
        for posicion in piezas:
            archivo.write(f'{piezas[posicion]},{posicion[0]};{posicion[1]}\n')


def cargar_nivel(TAMANIO):
    """
    DOC: Carga el ultimo nivel guardado desde un archivo CSV
    """
    tablero = [['' for _ in range(TAMANIO)] for _ in range(TAMANIO)]
    inicial = []

    with open('Shape-Shifter-Chess/ultimo_nivel.csv') as archivo:
        nivel = archivo.readline().rstrip()
        for fila in archivo:
            pieza, posicion = fila.rstrip().split(',')
            x, y = posicion.split(';')

            if pieza[::-1][0] == 'r':
                inicial = [pieza[:-2], int(x), int(y)]
            tablero[int(x)][int(y)] = pieza
    if nivel == '':
        return None
    return int(nivel), tablero, inicial


def cargar():
    """
    DOC: Pregunta al usuario si quiere cargar el ultimo nivel guardado,
    devuelve un tipo de dato bool
    """
    cargar = gamelib.input("¿Cargar el ultimo nivel guardado? (s/n): ")

    if cargar is None:
        return False

    while cargar not in 'sn' or cargar == '':
        gamelib.say("Ingrese comandos del tipo 's/n'")
        cargar = gamelib.input("¿Cargar el ultimo nivel guardado? (s/n): ")

        if cargar is None:
            return False

    if cargar == 's':
        return True
    return False
