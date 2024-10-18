import time
from multiprocessing import Process
from visualisations.visualisation import start_drawing1, start_drawing2

def run_implementation1():
    """Lance l'implémentation 1 (récursive) dans une fenêtre séparée."""
    start_time = time.time()
    start_drawing1(size=800, depth=4)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print(f"Durée d'exécution de l'implémentation 1: {execution_time:.2f} ms")

def run_implementation2():
    """Lance l'implémentation 2 (itérative) dans une autre fenêtre."""
    start_time = time.time()
    start_drawing2(size=800, depth=4)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print(f"Durée d'exécution de l'implémentation 2: {execution_time:.2f} ms")

if __name__ == "__main__":
    # Créer deux processus pour exécuter les deux implémentations en parallèle
    process1 = Process(target=run_implementation1)
    process2 = Process(target=run_implementation2)

    # Démarrer les deux processus
    process1.start()
    process2.start()

    # Attendre que les deux processus se terminent
    process1.join()
    process2.join()

    print("Les deux implémentations sont terminées.")
