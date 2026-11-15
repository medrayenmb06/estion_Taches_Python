taches = []


def ajouter_tache():
    titre = input("Titre de la tâche : ").strip()

    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
    else:
        taches.append(titre)
        print("Tâche ajoutée avec succès.")


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche pour le moment.")
    else:
        print("\n--- LISTE DES TÂCHES ---")
        for numero, titre in enumerate(taches, start=1):
            print(f"{numero}. {titre}")


def rechercher_tache():
    mot_cle = input("Mot-clé à rechercher : ").strip().lower()

    if mot_cle == "":
        print("Veuillez saisir un mot-clé.")
        return

    resultats = []
    for numero, titre in enumerate(taches, start=1):
        if mot_cle in titre.lower():
            resultats.append((numero, titre))

    if len(resultats) == 0:
        print("Aucune tâche trouvée.")
    else:
        print("\n--- RÉSULTATS DE LA RECHERCHE ---")
        for numero, titre in resultats:
            print(f"{numero}. {titre}")


def afficher_menu():
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")


while True:
    afficher_menu()
    choix = input("Votre choix : ").strip()

    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        rechercher_tache()
    elif choix == "0":
        print("Au revoir !")
        break
    else:
        print("Erreur : choix invalide. Réessayez.")
