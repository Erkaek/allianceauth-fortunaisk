# FortunaISK

FortunaISK est un plugin pour Alliance Auth qui gère une loterie mensuelle. 
Les joueurs achètent des tickets en envoyant des ISK au wallet de la corporation avec une référence spécifique.

## Installation

1. Clonez ce dépôt dans votre environnement Alliance Auth.
2. Ajoutez `fortunaisk` à `INSTALLED_APPS` dans `settings.py`.
3. Exécutez `python manage.py migrate`.
4. Redémarrez votre serveur.

## Fonctionnalités

- Vérification automatique des paiements via ESI.
- Configuration simple du prix des tickets et de la référence unique.
