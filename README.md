# Introducción al Desarrollo de Software - cátedra Essaya (75.40 / 95.14)

- Para toda la cursada el lenguaje usado fue Python.
- Tambien se hizo uso de una API llamada [Gamelib](https://github.com/dessaya/python-gamelib) desarrollada por el jefe de cátedra, con la cual se completaron las entregas.

```python
# Un simple ejemplo que muestra en pantalla "Hello World!"

import gamelib

def main():
    gamelib.resize(300, 300)

    gamelib.draw_begin()
    gamelib.draw_text('Hello world!', 150, 150)
    gamelib.draw_end()

    # wait until the user presses any key
    gamelib.wait(gamelib.EventType.KeyPress)

gamelib.init(main)
```

## Entregas 2022C1
- [EJ2](https://github.com/Igris-1/Algoritmos-y-programacion-I/tree/main/EJ2) - Five in line
- [TP1](https://github.com/Igris-1/Algoritmos-y-programacion-I/tree/main/Fifteen) - Fifteen
- [TP2](https://github.com/Igris-1/Algoritmos-y-programacion-I/tree/main/Shape-Shifter-Chess) - Shape Shifter Chess
- [TP3](https://github.com/Igris-1/Algoritmos-y-programacion-I/tree/main/Flood) - Flood

### Correr cualquier entrega
```
$ python3 main.py
```
