import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from implementations.implementation2 import SierpinskiCarpetIterative

def test_initialization():
    """Test de l'initialisation de la classe SierpinskiCarpetIterative."""
    carpet = SierpinskiCarpetIterative(size=300, depth=4)
    assert carpet.size == 300
    assert carpet.depth == 4

def test_draw_square():
    """Test de la méthode draw_square pour dessiner un carré."""
    carpet = SierpinskiCarpetIterative(size=300, depth=4)
    # Vérifie la méthode draw_square
    try:
        carpet.draw_square(0, 0, 100)  # Dessine un carré de 100x100
    except Exception as e:
        pytest.fail(f"draw_square raised an exception: {e}")

def test_draw_carpet_base_case():
    """Test de la méthode draw_carpet avec profondeur 0."""
    carpet = SierpinskiCarpetIterative(size=300, depth=0)
    # Vérifie que draw_carpet ne lève pas d'exception
    try:
        carpet.draw_carpet()
    except Exception as e:
        pytest.fail(f"draw_carpet raised an exception in base case: {e}")

def test_draw_carpet_recursive_call():
    """Test de la méthode draw_carpet pour vérifier les appels récursifs."""
    carpet = SierpinskiCarpetIterative(size=300, depth=2)
    try:
        carpet.draw_carpet()  # Teste la génération du tapis
        assert carpet.depth == 2  # La profondeur devrait rester à 2
    except Exception as e:
        pytest.fail(f"draw_carpet raised an exception during recursive call: {e}")

def test_start_drawing():
    """Test de la méthode start_drawing pour s'assurer qu'elle s'exécute sans erreur."""
    carpet = SierpinskiCarpetIterative(size=300, depth=1)
    try:
        carpet.start_drawing()  # Teste le démarrage du dessin
    except Exception as e:
        pytest.fail(f"start_drawing raised an exception: {e}")

