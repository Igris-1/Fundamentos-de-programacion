import gamelib
import logica


# Ajustar el tamaño de la ventana
TAMANIO = 10 # min = 4, max = lo que de

def main():
    gamelib.title("Algo I EJ2 Nat")
    tablero = logica.inicializar_tablero(TAMANIO)
    turno = 0

    gamelib.resize(TAMANIO * 25, TAMANIO * 25 + 20)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        logica.juego_mostrar(tablero, turno, TAMANIO)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos
        # (si el usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            tablero, turno = logica.juego_actualizar(tablero, x, y, turno)

gamelib.init(main)