import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from implementations.implementation1 import SierpinskiCarpet


def test_initialization():
    """Test de l'initialisation de la classe SierpinskiCarpet."""
    carpet = SierpinskiCarpet(size=300, depth=4)
    assert carpet.size == 300
    assert carpet.depth == 4
    assert carpet.t is not None  # Vérifie que le pinceau a été initialisée

def test_draw_square():
    """Test de la méthode draw_square pour dessiner un carré."""
    carpet = SierpinskiCarpet(size=300, depth=4)
    # Vérifie la méthode draw_square
    try:
        carpet.draw_square(0, 0, 100)  # Dessine un carré de 100x100
    except Exception as e:
        pytest.fail(f"draw_square raised an exception: {e}")

def test_draw_carpet_base_case():
    """Test de la méthode draw_carpet avec profondeur 0."""
    carpet = SierpinskiCarpet(size=300, depth=0)
    # Vérifie que draw_square est appelé correctement et dessine qu'un c&rré
    try:
        carpet.draw_carpet(0, 0, 300, 0)
    except Exception as e:
        pytest.fail(f"draw_carpet raised an exception in base case: {e}")

def test_draw_carpet_recursive_call():
    """Test de la méthode draw_carpet pour vérifier les appels récursifs."""
    carpet = SierpinskiCarpet(size=300, depth=2)
    try:
        carpet.draw_carpet(0, 0, 300, 2)
        assert carpet.depth == 2  # Profondeur est correcte ?
    except Exception as e:
        pytest.fail(f"draw_carpet raised an exception during recursive call: {e}")
