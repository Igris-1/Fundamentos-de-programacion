import random
from cola import Cola


class Flood:
    """
    Clase para administrar un tablero de N colores.
    """
    def __init__(self, alto, ancho):
        """
        Genera un nuevo Flood de un mismo color con las dimensiones dadas.

        Argumentos:
            alto, ancho (int): Tamaño de la grilla.
        """
        self.alto = alto
        self.ancho = ancho
        self.tablero = [['' for _ in range(ancho)] for _ in range(alto)]


    def mezclar_tablero(self, n_colores):
        """
        Asigna de forma completamente aleatoria hasta `n_colores` a lo largo de
        las casillas del tablero.

        Argumentos:
            n_colores (int): Cantidad maxima de colores a incluir en la grilla.
        """
        for i in range(self.alto):
            for j in range(self.ancho):
                self.tablero[i][j] = random.randint(0, n_colores - 1)


    def obtener_color(self, fil, col):
        """
        Devuelve el color que se encuentra en las coordenadas solicitadas.

        Argumentos:
            fil, col (int): Posiciones de la fila y columna en la grilla.

        Devuelve:
            Color asignado.
        """
        return self.tablero[fil][col]


    def obtener_posibles_colores(self):
        """
        Devuelve una secuencia ordenada de todos los colores posibles del juego.
        La secuencia tendrá todos los colores posibles que fueron utilizados
        para generar el tablero, sin importar cuántos de estos colores queden
        actualmente en el tablero.

        Devuelve:
            iterable: secuencia ordenada de colores.
        """
        colores = []
        for i in self.tablero:
            for j in i:
                if j not in colores:
                    colores.append(j)

        return sorted(colores)


    def dimensiones(self):
        """
        Dimensiones de la grilla (filas y columnas)

        Devuelve:
            (int, int): alto y ancho de la grilla en ese orden.
        """
        return self.alto, self.ancho


    def cambiar_color(self, color_nuevo):
        """
        Asigna el nuevo color al Flood de la grilla. Es decir, a todas las
        coordenadas que formen un camino continuo del mismo color comenzando
        desde la coordenada origen en (0, 0) se les asignará `color_nuevo`

        Argumentos:
            color_nuevo: Valor del nuevo color a asignar al Flood.
        """
        color_a = self.tablero[0][0]
        if color_a != color_nuevo:
            self.cambiar_color_rec(color_a, color_nuevo, 0, 0)


    def cambiar_color_rec(self, color_a, color_nuevo, fil, col):
        """
        Recursivo: Cambia el color de todas las casillas que se encuentran en
        un camino continuo del mismo color que comienza en la coordenada
        (fil, col)
        """
        if 0 <= fil < self.alto and 0 <= col < self.ancho:
            if self.tablero[fil][col] == color_a:
                self.tablero[fil][col] = color_nuevo
                self.cambiar_color_rec(color_a, color_nuevo, fil, col + 1)
                self.cambiar_color_rec(color_a, color_nuevo, fil + 1, col)
                self.cambiar_color_rec(color_a, color_nuevo, fil, col - 1)
                self.cambiar_color_rec(color_a, color_nuevo, fil - 1, col)


    def clonar(self):
        """
        Devuelve:
            Flood: Copia del Flood actual
        """
        copia = Flood(self.alto, self.ancho)
        copia.tablero = [self.tablero[i][:] for i in range(len(self.tablero))]
        return copia


    def esta_completado(self):
        """
        Indica si todas las coordenadas de grilla tienen el mismo color

        Devuelve:
             bool: True si toda la grilla tiene el mismo color
        """
        color_a = self.tablero[0][0]
        
        for fila in self.tablero:
            for color in fila:
                if color != color_a:
                    return False
        return True

    def posibles_mov(self):
        """
        Devuelve una Cola y la cantidad 'minima' de pasos para completar el flood
        """
        cola = Cola()
        num = 0

        while True:
            if self.esta_completado():
                return num, cola

            color_mayor_a, _ = self._obtener_color()
            self.cambiar_color(color_mayor_a)
            cola.encolar(color_mayor_a)
            num += 1


    def _obtener_color(self):
        """
        Devuelve el color que mas area/casilleros le agrega al flood actual
        """
        colores = self.obtener_posibles_colores()
        area_inicial = self.clonar().area_actual(0, 0, {})
        areas = []

        for color in colores:
            copia = self.clonar()
            copia.cambiar_color(color)
            area = copia.area_actual(0, 0, {})

            if area + area_inicial > area_inicial:
                areas.append([color, area])

        return max(areas, key=lambda x: x[1])


    def area_actual(self, fil, col, d):
        """
        Recursivo: devuelve el area actual del flood
        sin peretir casilleros
        """
        color_a = self.tablero[0][0]

        if 0 <= fil < self.alto and 0 <= col < self.ancho:
            if self.tablero[fil][col] == color_a:
                if (fil, col) not in d:
                    d[(fil, col)] = 1
                    return 1 + self.area_actual(fil, col + 1, d) + self.area_actual(fil + 1, col, d) + self.area_actual(fil, col - 1, d) + self.area_actual(fil - 1, col, d)
        return 0
