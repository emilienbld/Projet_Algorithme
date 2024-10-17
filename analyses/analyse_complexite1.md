# Analyse de la Complexité - Implémentation 1 (SierpinskiCarpet)

## Introduction

Cette analyse examine la complexité temporelle et spatiale de la première implémentation du Tapis de Sierpinski. L'algorithme dessine récursivement un carré central et répète ce processus pour chacun des huit sous-carrés restants jusqu'à atteindre la profondeur donnée. Cette analyse inclut une discussion sur les récursions et l'impact sur les performances.

---

## Complexité Temporelle

L'algorithme utilise une approche récursive pour dessiner le tapis de Sierpinski. À chaque niveau de profondeur, il divise le carré initial en 9 sous-carrés et appelle la fonction récursive pour 8 de ces sous-carrés, en ignorant le carré central.

---

### Analyse récursive :

1. **Profondeur 0** : Il n'y a pas de récursion, un seul carré est dessiné.
2. **Profondeur 1** : La fonction divise le carré en 9 sous-carrés et dessine 8 sous-carrés.
3. **Profondeur 2** : Pour chacun des 8 sous-carrés, la fonction les divise à nouveau en 9 et dessine 8 sous-carrés pour chaque division, soit 8 x 8 carrés.
4. **Profondeur `n`** : La fonction appelle 8 sous-carrés récursivement à chaque niveau. Cela signifie qu'à chaque profondeur `d`, le nombre total de carrés dessinés est de `8^d`.

---

### Calcul de la complexité :

La complexité temporelle totale dépend du nombre de carrés dessinés, qui est de l'ordre de `O(8^d)` pour une profondeur `d`. Ainsi, la **complexité temporelle** est :

**O(8^d)**

Cela signifie que plus la profondeur `d` augmente, plus le temps nécessaire à l'algorithme pour dessiner tous les sous-carrés croît exponentiellement.

---

### Impact de la taille du carré :

Bien que la taille du carré puisse varier, l'algorithme divise toujours le carré en 9 parties égales à chaque niveau de récursion. Le temps nécessaire pour dessiner un carré est constant, et donc l'impact sur la complexité temporelle est négligeable par rapport à la profondeur récursive.

---

## Complexité Spatiale

La complexité spatiale est déterminée par la profondeur de la pile d'appels récursifs.

1. À chaque appel récursif, la fonction stocke l'état actuel des coordonnées et de la taille du carré sur la pile d'exécution.
2. Le nombre maximum de niveaux de récursion est égal à la profondeur `d`.

Ainsi, la **complexité spatiale** est directement proportionnelle à la profondeur de récursion et est de l'ordre de :

**O(d)**

Cela signifie que la mémoire requise augmente linéairement avec la profondeur `d`, car chaque appel récursif occupe un espace supplémentaire dans la pile d'exécution.

---

## Conclusion

Pour cette première implémentation de l'algorithme du Tapis de Sierpinski, nous pouvons conclure les complexités suivantes :

- **Complexité Temporelle** : O(8^d), où `d` est la profondeur du tapis.
- **Complexité Spatiale** : O(d), en raison des appels récursifs.

Ces complexités montrent que cette implémentation est gourmande en temps pour des profondeurs élevées, car le nombre d'appels récursifs croît de manière exponentielle. Cependant, la complexité spatiale reste modérée, étant linéaire par rapport à la profondeur du tapis.
