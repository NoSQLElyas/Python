import random

# Liste de mots pour le jeu
mots = ["python", "pendu", "programmation", "ordinateur", "jeu", "apprentissage", "arbre", "maison", "voiture", "ordinateur", "chien", "chat", "soleil", "lune", "montagne", "rivière", "plage", "fleur", "oiseau", "livre", "école", "travail", "musique", "film", "sport", "amour"]

# Sélection aléatoire d'un mot
mot_a_deviner = random.choice(mots)

# Initialisation des variables
lettres_trouvees = []
mot_trouve = "_" * len(mot_a_deviner)
essais_restants = 7

# Fonction pour afficher le mot partiellement découvert
def afficher_mot():
    for lettre in mot_trouve:
        print(lettre, end=" ")
    print("\n")

# Boucle principale du jeu
while essais_restants > 0 and "_" in mot_trouve:
    print("Mot à deviner :")
    afficher_mot()
    print(f"Essais restants : {essais_restants}")
    lettre = input("Entrez une lettre : ").lower()

    if lettre in lettres_trouvees:
        print("Vous avez déjà deviné cette lettre. Essayez une autre lettre.")
        continue

    if lettre in mot_a_deviner:
        print("Bonne devinette !")
        lettres_trouvees.append(lettre)
        nouveau_mot = ""
        for i in range(len(mot_a_deviner)):
            if mot_a_deviner[i] == lettre:
                nouveau_mot += lettre
            else:
                nouveau_mot += mot_trouve[i]
        mot_trouve = nouveau_mot
    else:
        print("Désolé, cette lettre ne fait pas partie du mot à deviner.")
        essais_restants -= 1

if "_" not in mot_trouve:
    print(f"Félicitations ! Vous avez deviné le mot : {mot_a_deviner}")
else:
    print(f"Désolé, vous avez épuisé tous vos essais. Le mot à deviner était : {mot_a_deviner}")