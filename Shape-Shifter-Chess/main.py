import logica
import gamelib

# Se pueden agregar o quitar piezas del archivo movimientos.csv y
# esto va a seguir funcionando

# min = 8 (sino el texto queda fuera), max = lo que de, en numeros pares
TAMANIO = 8


def main():
    """DOC: Contiene el codigo de control del juego"""
    gamelib.title("Shape Shifter Chess")
    tablero = logica.inicializar_tablero(TAMANIO)
    gamelib.resize(TAMANIO * 44, TAMANIO * 44 + 26)

    movimientos, piezas = logica.movimientos('Shape-Shifter-Chess/movimientos.csv', tablero)
    nivel = 1
    inicial = logica.agregar_piezas(tablero, nivel, movimientos, piezas)
    _tablero, _inicial = [tablero[i][:]
                          for i in range(len(tablero))], inicial[:]

    cargar = logica.cargar()

    if cargar:
        if logica.cargar_nivel(TAMANIO) == None:
            gamelib.say("No hay niveles guardados, iniciara un nuevo juego")
        else:
            nivel, tablero, inicial = logica.cargar_nivel(TAMANIO)

    _tablero, _inicial = [tablero[i][:]
                          for i in range(len(tablero))], inicial[:]
    logica.guardar_nivel(nivel, _tablero)

    while gamelib.is_alive():
        if logica.gano(tablero):
            nivel += 1
            tablero = logica.inicializar_tablero(TAMANIO)
            inicial = logica.agregar_piezas(
                tablero, nivel, movimientos, piezas)
            _tablero, _inicial = [tablero[i][:]
                                  for i in range(len(tablero))], inicial[:]
            logica.guardar_nivel(nivel, _tablero)

        gamelib.draw_begin()
        logica.juego_mostrar(tablero, TAMANIO, nivel, inicial, movimientos)
        gamelib.draw_end()

        ev = gamelib.wait()
        if not ev:
            break

        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
            x, y = ev.x, ev.y
            tablero, inicial = logica.actualizar(
                tablero, x, y, inicial, movimientos)

        elif ev.type == gamelib.EventType.KeyPress:
            if ev.key == 'e':
                break

            elif ev.key == 'z':
                tablero, inicial = [_tablero[i][:]
                                    for i in range(len(tablero))], _inicial[:]

            elif ev.key == 'c':
                nivel, tablero, inicial = logica.cargar_nivel(TAMANIO)
                _tablero, _inicial = [tablero[i][:]
                                      for i in range(len(tablero))], inicial[:]


gamelib.init(main)
