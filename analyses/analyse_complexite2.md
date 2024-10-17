# Analyse de la Complexité - Implémentation 2 (SierpinskiCarpetIterative)

## Introduction

Cette analyse examine la complexité temporelle et spatiale de la deuxième implémentation du Tapis de Sierpinski, qui utilise une approche itérative. L'algorithme divise un carré central et répète ce processus pour chacun des sous-carrés restants jusqu'à atteindre la profondeur donnée. Cette analyse inclut une discussion sur l'impact de l'itération sur les performances par rapport à l'approche récursive.

---

## Complexité Temporelle

L'algorithme utilise une approche itérative pour dessiner le tapis de Sierpinski. À chaque niveau de profondeur, il divise le carré initial en 9 sous-carrés et dessine 8 de ces sous-carrés, tout en ignorant le carré central. L'itération permet de gérer le dessin sans avoir recours à des appels récursifs, ce qui a un impact sur la complexité temporelle.

---

### Analyse itérative :

1. **Profondeur 0** : Il n'y a pas de itération, un seul carré est dessiné.
2. **Profondeur 1** : L'algorithme dessine 8 sous-carrés.
3. **Profondeur 2** : Pour chaque sous-carré, l'algorithme dessine à nouveau 8 sous-carrés, soit 8 x 8 carrés.
4. **Profondeur `d`** : À chaque profondeur `d`, le nombre total de carrés dessinés reste de `8^d`.

---

### Calcul de la complexité :

La complexité temporelle totale dépend du nombre de carrés dessinés, qui est de l'ordre de `O(8^d)` pour une profondeur `d`. Ainsi, la **complexité temporelle** est :

**O(8^d)**

Cette complexité est similaire à celle de l'implémentation récursive. L'itération permet cependant de réduire l'impact sur la mémoire, car il n'y a pas de pile d'appels récursifs, mais le temps nécessaire pour dessiner tous les sous-carrés croît toujours exponentiellement avec la profondeur `d`.

---

### Impact de la taille du carré :

Comme dans l'implémentation précédente, la taille du carré peut varier, mais l'algorithme divise toujours le carré en 9 parties égales à chaque niveau. Le temps nécessaire pour dessiner un carré reste constant, et donc l'impact sur la complexité temporelle est négligeable par rapport à la profondeur itérative.

---

## Complexité Spatiale

La complexité spatiale est déterminée par l'utilisation de la mémoire pour gérer les variables dans la boucle itérative. Contrairement à l'approche récursive, l'itération ne nécessite pas de mémoire supplémentaire pour la pile d'appels.

1. La mémoire utilisée pour les coordonnées et la taille des carrés est constante.
2. L'algorithme utilise des variables locales pour suivre la position et la profondeur actuelle, sans stocker plusieurs niveaux d'état sur la pile.

Ainsi, la **complexité spatiale** est de l'ordre de :

**O(1)**

Cela signifie que la mémoire requise ne dépend pas de la profondeur `d`, mais reste constante, indépendamment du niveau de profondeur.

---

## Conclusion

Pour cette deuxième implémentation de l'algorithme du Tapis de Sierpinski, nous pouvons conclure les complexités suivantes :

- **Complexité Temporelle** : O(8^d), où `d` est la profondeur du tapis.
- **Complexité Spatiale** : O(1), grâce à l'utilisation d'une approche itérative sans récursion.

Ces complexités montrent que, bien que cette implémentation soit toujours gourmande en temps pour des profondeurs élevées, elle présente un avantage notable en termes de complexité spatiale, en n'utilisant qu'un espace constant pour le stockage des variables.
