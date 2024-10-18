import turtle  # Bibliothèque turtle pour le dessin

class SierpinskiCarpetIterative:
    def __init__(self, size, depth):
        self.size = size  # Taille du tapis
        self.depth = depth  # Profondeur
        self.stack = []  # Utilise une pile pour simuler la récursion dans une implémentation itérative

    def draw_square(self, x, y, size):
        """
        Dessine un carré à la position (x, y) de la taille choisie.
        """
        turtle.penup()  # Lève le stylo pour déplacer la tortue sans dessiner
        turtle.goto(x, y)  # Déplace la tortue à la position (x, y)
        turtle.pendown()  # Descendre le stylo pour dessiner
        for _ in range(4):  # Dessine un carré
            turtle.forward(size)  # Avance en fonction de la taille choisie
            turtle.right(90)  # Droite 90°

    def draw_carpet(self):
        """
        Génère le Tapis de façon itérative avec une Stack.
        """
        # Empile le premier carré de départ centré sur l'écran
        self.stack.append((-self.size / 2, self.size / 2, self.size, 0))

        while self.stack:
            # Dépile les coordonnées, taille et profondeur actuelles
            x, y, size, current_depth = self.stack.pop()
            
            if current_depth == self.depth:
                # Si on a atteint la profondeur maximale, on dessine le carré
                self.draw_square(x, y, size)
            else:
                # Sinon, divise le carré en 9 sous-carrés et empile les 8 sous-carrés sans le centre
                new_size = size / 3  # Taille des sous-carrés
                # Coordonnées des 8 sous-carrés (en ignorant le centre)
                offsets = [
                    (0, 0), (new_size, 0), (2 * new_size, 0),
                    (0, -new_size), (2 * new_size, -new_size),
                    (0, -2 * new_size), (new_size, -2 * new_size), (2 * new_size, -2 * new_size)
                ]
                
                # Empile les 8 sous-carrés avec leurs nouvelles coordonnées et tailles
                for dx, dy in offsets:
                    self.stack.append((x + dx, y + dy, new_size, current_depth + 1))
