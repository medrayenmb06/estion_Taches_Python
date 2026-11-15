# Guide de réalisation Git / GitHub

Ce guide suit les consignes de la fiche projet. Remplace les valeurs entre chevrons par tes informations.

## 1. Préparer le dossier
1. Décompresse `Gestion_Taches_Python.zip`.
2. Ouvre le dossier `Gestion_Taches_Python` dans VS Code.
3. Ouvre `main.py` et clique sur **Run Python File** pour tester le programme.

## 2. Faire au moins trois commits cohérents

Les commits doivent montrer de vraies étapes du travail. Pour avoir un historique progressif, réalise les commits pendant que tu développes :

### Commit 1 — première version (menu, ajout et affichage)
Commence par une première version de `main.py` avec la liste `taches`, le menu, l'ajout et l'affichage. Teste-la, puis :
```bash
git init
git status
git add main.py
git commit -m "Ajouter le programme initial"
```

### Commit 2 — documentation
Crée/complète `README.md` avec la description, les fonctionnalités et les étapes d'exécution :
```bash
git add README.md
git commit -m "Documenter le projet"
```

### Commit 3 — recherche
Ajoute la fonction de recherche et son choix dans le menu de `main.py` (le `main.py` fourni dans ce dossier contient déjà la version finale avec cette fonction) :
```bash
git add main.py
git commit -m "Ajouter la recherche de taches"
```

Vérifie l'historique :
```bash
git log --oneline
```

Si tu as déjà copié le `main.py` final avant le premier commit, ne prétends pas que les commits représentent des étapes qui n'ont pas réellement eu lieu. Fais plutôt de vraies petites améliorations successives et committe chaque étape.

## 3. Créer le dépôt GitHub et faire le premier push
1. Sur GitHub, crée un nouveau dépôt vide (ne coche pas l'ajout automatique d'un README).
2. Copie l'adresse HTTPS du dépôt.
3. Dans Git Bash, depuis le dossier du projet, exécute :
```bash
git branch -M main
git remote add origin https://github.com/<COMPTE>/<DEPOT>.git
git remote -v
git push -u origin main
```
Remplace `<COMPTE>` et `<DEPOT>` par ton compte et le nom du dépôt. Si `origin` existe déjà, ne refais pas `git remote add origin`; vérifie avec `git remote -v`.

## 4. Publier une mise à jour après le premier push
Après le premier push, fais une petite amélioration réelle, par exemple ajoute une ligne utile dans `README.md` qui précise que la recherche ne distingue pas les majuscules des minuscules. Puis :
```bash
git add README.md
git commit -m "Preciser le fonctionnement de la recherche"
git push
```

## 5. Vérifications et captures pour Blackboard
Prends des captures d'écran de :
- `git log --oneline` : les commits sont visibles.
- `git remote -v` : l'adresse du dépôt GitHub est visible.
- La page GitHub : `main.py` et `README.md` sont visibles.
- La mise à jour : le dernier commit apparaît sur GitHub après le second push.

Le rapport Word/PDF demandé doit contenir les noms des deux étudiants, le lien GitHub, les captures et les explications ci-dessous.

## 6. Explication des commandes
- `git add` : prépare les fichiers modifiés pour le prochain commit.
- `git commit` : enregistre localement un point de l'historique du projet.
- `git push` : envoie les commits locaux vers le dépôt GitHub.

## Important
Ne mets pas de faux noms, de faux lien GitHub ou de fausses captures dans le rapport. Complète ces éléments après avoir fait le travail réel.
