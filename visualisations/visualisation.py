from implementations.implementation1 import SierpinskiCarpetRecursive
from implementations.implementation2 import SierpinskiCarpetIterative
import turtle

def start_drawing1(size, depth):
    """Démarre le dessin pour l'implémentation 1 (récursive)."""
    carpet = SierpinskiCarpetRecursive(size, depth)
    carpet.t.penup()  # Lève le stylo
    carpet.t.goto(-size // 2, size // 2)  # Centre le tapis sur l'écran
    carpet.t.pendown()  # Abaisse le stylo
    # Commence à dessiner le tapis
    carpet.draw_carpet(-size // 2, size // 2, size, depth)
    turtle.update()
    turtle.done()

def start_drawing2(size, depth):
    """Démarre le dessin pour l'implémentation 2 (itérative)."""
    carpet = SierpinskiCarpetIterative(size, depth)
    turtle.speed(0)  # Vitesse de dessin
    turtle.hideturtle()  # Cache le pinceau
    turtle.tracer(0, 0)  # Désactivation du traçage pour qe ça aille plus vite
    # Commence à dessiner le tapis
    carpet.draw_carpet()
    turtle.update()
    turtle.done()
