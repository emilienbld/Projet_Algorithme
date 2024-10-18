import time
from visualisations.visualisation import start_drawing1, start_drawing2

if __name__ == "__main__":
    # Exécution de l'implémentation 1 (récursive)
    start_time = time.time()
    start_drawing1(size=800, depth=4)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print(f"Durée d'exécution de l'implémentation 1: {execution_time:.2f} ms")

    # Exécution de l'implémentation 2 (itérative)
    start_time = time.time()
    start_drawing2(size=800, depth=4)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print(f"Durée d'exécution de l'implémentation 2: {execution_time:.2f} ms")
