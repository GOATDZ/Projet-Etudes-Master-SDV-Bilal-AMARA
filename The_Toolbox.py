"""
Copyright© 28/06/2024, Bilal AMARA MSI C Cybersecurite 2024
Version : 1.0
Projet d'Études
"""

import subprocess  # Module pour exécuter des sous-processus
import os  # Module pour les opérations sur le système de fichiers
from affichage_menu import (Display_menu_title, Display_menu_options, 
                            Display_menu_Black_box_test, Display_menu_Grey_box_test, 
                            Display_menu_White_box_test)  # Importation des fonctions d'affichage des menus
from colorama import init  # Module pour la gestion des couleurs dans le terminal

# Détermine le répertoire courant du script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Point d'entrée principal du script
if __name__ == "__main__":

    init()  # Initialise le module colorama pour gérer les couleurs du terminal
    Display_menu_title()  # Affiche le titre du menu principal
    Display_menu_options()  # Affiche les options du menu principal
    
    # Demande à l'utilisateur de choisir une option dans le menu principal
    option = int(input(">>> Choose an option\n>>> "))  

    # Boucle principale qui continue tant que l'utilisateur ne choisit pas l'option de sortie (99)
    while option != 99:  

        if option == 1:  # Option pour les tests Black Box
            while True:
                Display_menu_Black_box_test()  # Affiche le menu des tests Black Box
                subOption = str(input(">>> Choose an option\n>>> ")).strip()  # Demande à l'utilisateur de choisir une sous-option
                if subOption == 'z':  # Option pour revenir au menu précédent
                    break

                # Exécute les scripts correspondants aux sous-options choisies
                if subOption == 'a':  
                    subprocess.run(["python", os.path.join(current_dir, "modules/Scan_ip_os.py")])
                elif subOption == 'b': 
                    subprocess.run(["python", os.path.join(current_dir, "modules/scan_ports_services.py")])
                elif subOption == 'c':  
                    subprocess.run(["python", os.path.join(current_dir, "modules/domain_name.py")])
                elif subOption == 'd':  
                    subprocess.run(["python", os.path.join(current_dir, "modules/recherche_exploits.py")])
                elif subOption == 'e':  
                    subprocess.run(["python", os.path.join(current_dir, "modules/Rapport_Test_Black_Box.py")])
                else:
                    print("Invalid option. Please choose again.")  # Message en cas de choix invalide

        elif option == 2:  # Option pour les tests Grey Box
            while True:
                Display_menu_Grey_box_test()  # Affiche le menu des tests Grey Box
                subOption = str(input(">>> Choose an option\n>>> ")).strip()  # Demande à l'utilisateur de choisir une sous-option
                if subOption == 'z':  # Option pour revenir au menu précédent
                    break

                # Exécute les scripts correspondants aux sous-options choisies
                if subOption == 'a':  
                    subprocess.run(["python", os.path.join(current_dir, "modules/scan_vulnerabilite_os.py")])
                elif subOption == 'b':  
                    subprocess.run(["python", os.path.join(current_dir, "modules/scan_vulnerabilite_protocole.py")])
                elif subOption == 'c':  
                    subprocess.run(["python", os.path.join(current_dir, "modules/scan_vulnerable_os.py")])
                elif subOption == 'd':  
                    subprocess.run(["python", os.path.join(current_dir, "Rapport_Test_Grey_Box.py")])
                else:
                    print("Invalid option. Please choose again.")  # Message en cas de choix invalide

        elif option == 3:  # Option pour les tests White Box
            while True:
                Display_menu_White_box_test()  # Affiche le menu des tests White Box
                subOption = str(input(">>> Choose an option\n>>> ")).strip()  # Demande à l'utilisateur de choisir une sous-option
                if subOption == 'z':  # Option pour revenir au menu précédent
                    break

                # Exécute les scripts correspondants aux sous-options choisies
                if subOption == 'a':  
                    subprocess.run(["python", os.path.join(current_dir, "modules/password.py")])
                elif subOption == 'b':  
                    subprocess.run(["python", os.path.join(current_dir, "modules/bruteforce.py")])
                elif subOption == 'c':  
                    subprocess.run(["python", os.path.join(current_dir, "modules/Rapport_Test_White_Box.py")])
                else:
                    print("Invalid option. Please choose again.")  # Message en cas de choix invalide
        
        Display_menu_options()  # Ré-affiche les options du menu principal après chaque boucle
        option = int(input(">>> Choose an option\n>>> "))  # Demande à l'utilisateur de choisir une option
