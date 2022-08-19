from flood import Flood
from pila import Pila
from cola import Cola


class JuegoFlood:
    """
    Clase para administrar un Flood, junto con sus estados y acciones
    """

    def __init__(self, alto, ancho, n_colores):
        """
        Genera un nuevo JuegoFlood, el cual tiene un Flood y otros
        atributos para realizar las distintas acciones del juego.

        Argumentos:
            alto, ancho (int): Tamaño de la grilla del Flood.
            n_colores: Cantidad maxima de colores a incluir en la grilla.
        """
        self.flood = Flood(alto, ancho)
        self.flood.mezclar_tablero(n_colores)
        self.mejor_n_movimientos, _ = self._calcular_movimientos()
        self.n_movimientos = 0
        self.pasos_solucion = Cola()
        self.pasos = Pila()
        self.deshacer_rehacer = Pila()

    def cambiar_color(self, color):
        """
        Realiza la acción para seleccionar un color en el Flood, sumando a la
        cantidad de movimientos realizados y manejando las estructuras para
        deshacer y rehacer

        Argumentos:
            color (int): Nuevo color a seleccionar
        """
        actual = self.flood.clonar().tablero
        act_mod = self.flood.clonar()
        act_mod.cambiar_color(color)

        if actual != act_mod.tablero:
            self.pasos.apilar(self.flood.clonar())
            self.flood.cambiar_color(color)
            self.n_movimientos += 1

        while not self.deshacer_rehacer.esta_vacia():
            self.deshacer_rehacer.desapilar()

        if not self.pasos_solucion.esta_vacia() and self.pasos_solucion.ver_frente() == color:
            self.pasos_solucion.desencolar()
        else:
            self.pasos_solucion = Cola()

    def deshacer(self):
        """
        Deshace el ultimo movimiento realizado si existen pasos previos,
        manejando las estructuras para deshacer y rehacer.
        """
        if not self.pasos.esta_vacia():
            self.deshacer_rehacer.apilar(self.flood.clonar())
            self.flood = self.pasos.ver_tope()
            self.pasos.desapilar()
            self.n_movimientos -= 1
        self.pasos_solucion = Cola()
        return

    def rehacer(self):
        """
        Rehace el movimiento que fue deshecho si existe, manejando las
        estructuras para deshacer y rehacer.
        """
        if not self.deshacer_rehacer.esta_vacia():
            self.pasos.apilar(self.flood.clonar())
            self.flood = self.deshacer_rehacer.ver_tope()
            self.deshacer_rehacer.desapilar()
            self.n_movimientos += 1
        self.pasos_solucion = Cola()
        return

    def _calcular_movimientos(self):
        """
        Realiza una solución de pasos contra el Flood actual (en una Cola)
        y devuelve la cantidad de movimientos que llevó a esa solución.

        CRITERIOS: El color que más casilleros agregaría al flood actual.
                   El color que más casilleros agregaría al perímetro del flood actual.
                   El color con el tamaño de "isla adyacente al flood" más grande.

        Devuelve:
            int: Cantidad de movimientos que llevó a la solución encontrada.
            Cola: Pasos utilizados para llegar a dicha solución
        """
        copia = self.flood.clonar()
        num, pasos = copia.posibles_mov()
        return num, pasos

    def hay_proximo_paso(self):
        """
        Devuelve un booleano indicando si hay una solución calculada
        """
        return not self.pasos_solucion.esta_vacia()

    def proximo_paso(self):
        """
        Si hay una solución calculada, devuelve el próximo paso.
        Caso contrario devuelve ValueError

        Devuelve:
            Color del próximo paso de la solución
        """
        return self.pasos_solucion.ver_frente()

    def calcular_nueva_solucion(self):
        """
        Calcula una secuencia de pasos que solucionan el estado actual
        del flood, de tal forma que se pueda llamar al método `proximo_paso()`
        """
        _, self.pasos_solucion = self._calcular_movimientos()

    def dimensiones(self):
        return self.flood.dimensiones()

    def obtener_color(self, fil, col):
        return self.flood.obtener_color(fil, col)

    def obtener_posibles_colores(self):
        return self.flood.obtener_posibles_colores()

    def esta_completado(self):
        return self.flood.esta_completado()
