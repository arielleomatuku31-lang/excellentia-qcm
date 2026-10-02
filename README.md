# Excellentia — QCM de 100 questions

## 1. Installer Python
Installe Python 3.11 ou plus récent.

## 2. Installer les dépendances
Dans le dossier du projet :

```bash
pip install -r requirements.txt
```

## 3. Lancer le site

```bash
python app.py
```

Puis ouvre dans ton navigateur :

http://127.0.0.1:5000

## Code d'accès de démonstration

`EXCELLENTIA2026`

Tu peux le modifier dans `app.py` :

```python
ACCESS_CODE = "TON_NOUVEAU_CODE"
```

## Contenu

- 100 questions
- 20 Maths
- 20 Logique
- 20 Français
- 20 Anglais
- 20 Culture générale
- Chronomètre de 100 minutes
- Envoi automatique à la fin du temps
- Score sur 100
- Correction détaillée
- Mini-explication pour chaque question
- Difficultés moyenne, difficile et très difficile

## Important pour une vraie mise en ligne

Le code d'accès de cette V1 est stocké directement dans Python. Pour un site public, il faudra passer à une authentification côté serveur avec mot de passe haché, HTTPS et éventuellement une base de données.
