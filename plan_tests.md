PLAN DE TESTS – Système de notation patinage artistique

TODO : Compléter le plan de tests suivants : 

| # | Description du test          | vbase | notes                   | Résultat attendu | Résultat obtenu |
|---|------------------------------|-------|-------------------------|------------------|-----------------|
| 1 | Cas normal                   | 3.2   | [3,2,1,2,3,3,2,2,3]     | 5.63             | 5.63            |
| 2 | Plusieurs max/min identiques | 2.5   | [3,2,1,1,3,3,1,2,3]     | 4.64             | 4.64            |
| 3 | Notes négatives              | 1.0   | [3,-2,1,2,-3,3,-2,2,-3] | 1.14             | 1.14            |
| 4 | Liste invalide (taille)      | 3.0   | [3,2,1,2,3,3,2]         | Erreur           | Erreur          |
| 5 | Valeurs hors bornes          | 2.5   | [3,2,10,2,3,3,-20,2,50] | Erreur           | Erreur          |

