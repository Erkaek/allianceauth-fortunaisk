# FortunaISK

**FortunaISK** est un plugin pour [Alliance Auth](https://gitlab.com/allianceauth/allianceauth) permettant de gérer un système de loterie mensuelle. Les utilisateurs peuvent acheter des tickets en ISK via des paiements automatisés et participer à un tirage au sort à la fin de chaque mois.

## Fonctionnalités principales

- **Achat de tickets automatisé** via [allianceauth-corp-tools](https://github.com/Solar-Helix-Independent-Transport/allianceauth-corp-tools).
- **Gestion du pot** cumulatif (somme des ISK dépensés).
- **Tirage au sort** automatique le dernier jour de chaque mois.
- **Historique des gagnants** pour suivre l’évolution de la loterie.
- **Notifications Discord** au gagnant via webhooks.

## Prérequis

- Python 3.8+
- Alliance Auth 2.9+ (ou version compatible)
- Django 3.2+ (inclus avec Alliance Auth)
- [allianceauth-corp-tools](https://github.com/Solar-Helix-Independent-Transport/allianceauth-corp-tools) >= 1.0.0

## Fichiers du Module

### 1. `.gitignore`

*Déjà présenté ci-dessus.*

### 2. `LICENSE`

*Déjà présenté ci-dessus.*

### 3. `MANIFEST.in`

*Déjà présenté ci-dessus.*

### 4. `requirements.txt`

**Chemin** : `allianceauth-fortunaisk/requirements.txt`

```text
allianceauth>=2.9
django>=3.2
allianceauth-corp-tools>=1.0.0
