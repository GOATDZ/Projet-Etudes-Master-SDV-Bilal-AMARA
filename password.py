def difficulte_mdp(mot_de_passe, fichier_mots_communs):
    """
    Évalue la complexité d'un mot de passe en fonction de sa longueur, 
    de la diversité des caractères utilisés et de sa présence dans une 
    liste de mots de passe couramment utilisés.

    Paramètres :
    mot_de_passe (str): Le mot de passe à évaluer.
    fichier_mots_communs (str): Chemin vers un fichier contenant une liste 
                                de mots de passe couramment utilisés.

    Retourne :
    str: 'Faible', 'Moyenne' ou 'Forte' selon la complexité du mot de passe.
    """
    
    # Calculer la longueur du mot de passe
    longueur = len(mot_de_passe)
    
    # Vérifier la diversité des caractères (minuscules, majuscules, chiffres, caractères spéciaux)
    diversite = 0
    if any(c.islower() for c in mot_de_passe):
        diversite += 1
    if any(c.isupper() for c in mot_de_passe):
        diversite += 1
    if any(c.isdigit() for c in mot_de_passe):
        diversite += 1
    if any(not c.isalnum() for c in mot_de_passe):
        diversite += 1
    
    # Vérifier si le mot de passe est dans la liste des mots de passe courants
    try:
        with open(fichier_mots_communs, 'r') as file:
            mots_communs = file.read().splitlines()
        if mot_de_passe in mots_communs:
            return 'Faible'
    except FileNotFoundError:
        print(f"Erreur : le fichier {fichier_mots_communs} n'a pas été trouvé.")
        return 'Indéterminé'
    
    # Évaluer la complexité du mot de passe
    score = longueur + diversite * 2
    if score < 6:
        return 'Faible'
    elif score < 10:
        return 'Moyenne'
    else:
        return 'Forte'

if __name__ == "__main__":
    # Demander le mot de passe à l'utilisateur
    mot_de_passe = input("Entrez le mot de passe à évaluer : ")
    # Chemin vers le fichier des mots de passe courants
    fichier_mots_communs = "passwords.txt"
    
    # Évaluation de la complexité du mot de passe
    complexite = difficulte_mdp(mot_de_passe, fichier_mots_communs)
    print(f"La complexité du mot de passe '{mot_de_passe}' est : {complexite}")
