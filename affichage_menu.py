from colorama import Fore, Style  # Importation des modules pour la gestion des couleurs dans le terminal

# Fonction pour afficher le titre du menu principal
def Display_menu_title():
    displayInfo = f"""{Style.RESET_ALL}
{Fore.CYAN}   
                                                                ███    ███  █████  ███████ ████████ ███████ ██████      ███████ ██████  ██    ██     ██████  ██████  ███████ ███████ ███████ ███    ██ ████████ ███████                
                                                                ████  ████ ██   ██ ██         ██    ██      ██   ██     ██      ██   ██ ██    ██     ██   ██ ██   ██ ██      ██      ██      ████   ██    ██    ██          ██         
                                                                ██ ████ ██ ███████ ███████    ██    █████   ██████      ███████ ██   ██ ██    ██     ██████  ██████  █████   ███████ █████   ██ ██  ██    ██    ███████                
                                                                ██  ██  ██ ██   ██      ██    ██    ██      ██   ██          ██ ██   ██  ██  ██      ██      ██   ██ ██           ██ ██      ██  ██ ██    ██         ██     ██         
                                                                ██      ██ ██   ██ ███████    ██    ███████ ██   ██     ███████ ██████    ████       ██      ██   ██ ███████ ███████ ███████ ██   ████    ██    ███████                
                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                       
                                                                                            ████████ ██   ██ ███████     ████████  ██████   ██████  ██      ██████   ██████  ██   ██                                                   
                                                                                               ██    ██   ██ ██             ██    ██    ██ ██    ██ ██      ██   ██ ██    ██  ██ ██                                                    
                                                                                               ██    ███████ █████          ██    ██    ██ ██    ██ ██      ██████  ██    ██   ███                                                     
                                                                                               ██    ██   ██ ██             ██    ██    ██ ██    ██ ██      ██   ██ ██    ██  ██ ██                                                    
                                                                                               ██    ██   ██ ███████        ██     ██████   ██████  ███████ ██████   ██████  ██   ██                                                   
{Style.RESET_ALL}
 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                              
    """
    print(displayInfo)

# Fonction pour afficher les options du menu principal
def Display_menu_options():
    displayInfo = f"""
    {Fore.CYAN}[ 1 ]{Style.RESET_ALL}  - Black Box Test 
    {Fore.CYAN}[ 2 ]{Style.RESET_ALL}  - Grey Box Test 
    {Fore.CYAN}[ 3 ]{Style.RESET_ALL}  - White Box Test

    {Fore.RED}[ 99 ]{Style.RESET_ALL} - Exit program
    """
    print(displayInfo)

# Fonction pour afficher le menu des tests Black Box
def Display_menu_Black_box_test():
    displayInfo = f"""
  {Fore.CYAN}[ 1 ] - Black Box Test{Style.RESET_ALL}

        {Fore.CYAN}[ a ]{Style.RESET_ALL} - Scan IP et OS
        {Fore.CYAN}[ b ]{Style.RESET_ALL} - Scan Ports et Services
        {Fore.CYAN}[ c ]{Style.RESET_ALL} - Scan Nom de Domaine
        {Fore.CYAN}[ d ]{Style.RESET_ALL} - Recherche Exploits
        {Fore.CYAN}[ e ]{Style.RESET_ALL} - Générer rapport
        
        {Fore.RED}[ z ]{Style.RESET_ALL} - Go back
  """
    print(displayInfo)

# Fonction pour afficher le menu des tests Grey Box
def Display_menu_Grey_box_test():
    displayInfo = f"""
  {Fore.CYAN}[ 2 ] - Grey Box Test{Style.RESET_ALL}

        {Fore.CYAN}[ a ]{Style.RESET_ALL} - Scan OS Vulnérabilités
        {Fore.CYAN}[ b ]{Style.RESET_ALL} - Scan Ports Vulnérabilités
        {Fore.CYAN}[ c ]{Style.RESET_ALL} - San Vulnérabilités CVE
        {Fore.CYAN}[ d ]{Style.RESET_ALL} - Générer rapport
        
        {Fore.RED}[ z ]{Style.RESET_ALL} - Go back
  """
    print(displayInfo)

# Fonction pour afficher le menu des tests White Box
def Display_menu_White_box_test():
    displayInfo = f"""
  {Fore.CYAN}[ 3 ] - White Box Test{Style.RESET_ALL}

        {Fore.CYAN}[ a ]{Style.RESET_ALL} - Gestion et Test de mot de passe
        {Fore.CYAN}[ b ]{Style.RESET_ALL} - Brute force 
        {Fore.CYAN}[ c ]{Style.RESET_ALL} - Générer rapport

        {Fore.RED}[ z ]{Style.RESET_ALL} - Go back
 """
    print(displayInfo)
