# Tapis de Sierpinski - Visualisation Algorithmique

Ce projet propose deux implémentations pour générer et visualiser un **Tapis de Sierpinski**, une figure fractale. L'objectif est de comparer les deux approches algorithmique (récursive et itérative) en termes de performance et complexité.

---

## 1. Choix de l'algorithme

Le **Tapis de Sierpinski** est une figure fractale obtenue en divisant un carré en neuf sous-carrés de tailles égales, en supprimant le carré central, puis en répétant ce processus récursivement sur les huit sous-carrés restants. Nous avons choisi cet algorithme pour sa nature récursive, idéale pour illustrer différentes stratégies de résolution (récursion vs itération) et observer leurs impacts sur la performance.

---

## 2. Description simple de l'algorithme

Le Tapis de Sierpinski commence par un grand carré. À chaque étape :
1. On divise le carré en 9 parties égales.
2. On retire le carré central.
3. On répète le processus pour chaque sous-carré jusqu'à atteindre une profondeur prédéfinie.

Ainsi, à chaque étape, on crée un motif géométrique complexe de plus en plus détaillé.

---

## 3. Structures de données utilisées

- **Pile (stack)** : Utilisée dans l'implémentation itérative pour simuler la récursion. Chaque élément de la pile contient les coordonnées du carré, sa taille et sa profondeur actuelle.
- **Objet Turtle** : Utilisé dans les deux implémentations pour dessiner le motif du tapis dans une fenêtre graphique.

---

## 4. Utilisation de la POO dans les implémentations

Chaque implémentation est encapsulée dans une classe :
- **SierpinskiCarpet** (implémentation récursive) : 
  - Utilise la récursion naturelle pour dessiner les sous-carrés.
  - La méthode `draw_carpet` appelle récursivement elle-même.
  
- **SierpinskiCarpetIterative** (implémentation itérative) :
  - Utilise une pile pour gérer les sous-carrés à dessiner de manière itérative.
  - La méthode `draw_carpet` évite la récursion en ajoutant et en retirant des éléments de la pile.

Les deux classes incluent une méthode `draw_square` pour dessiner un carré, réutilisée dans chaque implémentation.

---

## 5. Différences de complexité entre les implémentations

### Implémentation 1 : Récursive
- **Complexité temporelle** : O(8^d), où `d` est la profondeur. L'algorithme divise chaque carré en 8 sous-carrés pour chaque profondeur, donc la croissance est exponentielle.
- **Complexité spatiale** : O(d), car la pile d'exécution doit conserver les informations sur la profondeur maximale de récursion.

### Implémentation 2 : Itérative
- **Complexité temporelle** : O(8^d), similaire à l'implémentation récursive, puisque le nombre de sous-carrés à dessiner reste identique.
- **Complexité spatiale** : O(8^d), car l'utilisation de la pile stocke toutes les informations des sous-carrés à chaque étape.

---

## 6. Exécuter les tests avec pytest

Le projet inclut des tests pour vérifier le bon fonctionnement des deux implémentations. Pour exécuter les tests, suivez ces étapes :

1. Assurez-vous d'avoir installé pytest : 
   ```bash
   pip install pytest
2. Exécutez les tests à partir du répertoire racine du projet :
   ```bash
   pytest tests/test_implementation1.py
   pytest tests/test_implementation2.py

Ces tests vérifient l'initialisation des classes, le bon déroulement des méthodes de dessin, et la récursivité correcte dans chaque implémentation.

---

## 7. Exécuter le code et visualiser les résultats

Pour exécuter les deux implémentations et observer le Tapis de Sierpinski :

1. Lancez le fichier main.py :
   ```bash
   python main.py

Cela ouvrira **deux fenêtres** Turtle distinctes, chacune affichant le dessin du Tapis de Sierpinski, l'une avec l'implémentation récursive et l'autre avec l'implémentation itérative. Le temps d'exécution de chaque méthode sera également affiché dans la console.

---

## 8. Dépendances et instructions spéciales

### Dépendances
- **Python 3.x**
- **turtle** : Bibliothèque standard de Python pour le dessin graphique.
- **pytest** : Utilisé pour les tests unitaires.

### Instructions spéciales
- Assurez-vous que Turtle est compatible avec votre environnement graphique (par exemple, sous macOS, lancez le script dans un terminal compatible).
- Si vous souhaitez modifier la taille du tapis ou la profondeur de récursion, vous pouvez ajuster les paramètres dans `main.py` pour chaque implémentation.

---

## Conclusion

Ce projet compare deux approches pour générer le Tapis de Sierpinski : une implémentation récursive et une itérative. La récursion est naturelle pour ce type de fractale, mais peut devenir inefficace à grande échelle, tandis que l'itération permet de contourner certaines limitations de la récursion, notamment en termes de mémoire, au prix d'une gestion explicite de la pile.
