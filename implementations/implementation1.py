import turtle  # Bibliothèque turtle pour le dessin

class SierpinskiCarpet:
    def __init__(self, size, depth):
        self.size = size  # Taille du tapis
        self.depth = depth  # Profondeur
        self.t = turtle.Turtle()  # Instance pour dessiner
        self.t.speed(0)  # Vitesse de dessin
        turtle.tracer(0, 0)  # Désactivation du traçage pour qe ça aille plus vite

    def draw_square(self, x, y, size):
        """
        Dessine un carré à la position (x, y) de la taille choisie.
        """
        self.t.penup()  # Lève le stylo pour se déplacer sans dessiner
        self.t.goto(x, y)  # Déplace la tortue à la position (x, y)
        self.t.pendown()  # Descendre le stylo pour dessiner
        for _ in range(4):  # Dessine un carré
            self.t.forward(size)  # Avance en focntion de la taille choisie
            self.t.right(90)  # Droite 90°

    def draw_carpet(self, x, y, size, depth):
        """
        Dessine le tapis de Sierpinski récursivement.
        """
        if depth == 0:  # Cas de base
            self.draw_square(x, y, size)
        else:
            new_size = size / 3  # Taille des sous-carrés
            # 8 sous-carrés autour du centre
            for i in range(3):
                for j in range(3):
                    if i == 1 and j == 1:
                        continue  # Comme ça le centre sera vide
                    # Dessiner les sous-carrés récursivement
                    self.draw_carpet(x + i * new_size, y - j * new_size, new_size, depth - 1)

    def start_drawing(self):
        """
        Démarre le processus de dessin du tapis.
        """
        self.t.penup()  # Lève le stylo
        self.t.goto(-self.size // 2, self.size // 2)  # Centre le tapis sur l'écran
        self.t.pendown()  # Abaisse le stylo
        # Commence à dessiner le tapis
        self.draw_carpet(-self.size // 2, self.size // 2, self.size, self.depth)
        turtle.update()
        turtle.done()

if __name__ == "__main__":
    # Exécution du dessin. Avec une grande taille pour voire les sous-carrés
    carpet = SierpinskiCarpet(size=800, depth=4)  # Création du tapis avec comme taille 800 et profondeur 4
    carpet.start_drawing()  # Démarre le dessin du tapis
