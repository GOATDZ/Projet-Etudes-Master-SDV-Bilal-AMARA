import whois
import time

def get_domain_info(domain_name, retries=3, delay=5):
    for attempt in range(retries):
        try:
            # Obtenir les informations WHOIS pour le domaine
            domain_info = whois.whois(domain_name)
            
            # Afficher les informations du domaine
            print("Informations sur le nom de domaine :")
            print(f"Nom de domaine : {domain_info.domain_name}")
            print(f"Enregistré par : {domain_info.registrar}")
            print(f"Date de création : {domain_info.creation_date}")
            print(f"Date d'expiration : {domain_info.expiration_date}")
            print(f"Serveurs de noms : {domain_info.name_servers}")
            print(f"Statut : {domain_info.status}")
            print(f"Emails de contact : {domain_info.emails}")
            print(f"Organisation : {domain_info.org}")
            print(f"Pays : {domain_info.country}")
            print(f"Ville : {domain_info.city}")
            print(f"Adresse : {domain_info.address}")
            print(f"Code postal : {domain_info.zipcode}")
            break  # Sortir de la boucle si la requête réussit
        except whois.parser.PywhoisError as e:
            print(f"Une erreur est survenue : {e}")
            break  # Sortir de la boucle si une erreur spécifique liée à whois se produit
        except Exception as e:
            print(f"Une erreur est survenue lors de la tentative {attempt + 1} de {retries}: {e}")
            if attempt < retries - 1:
                time.sleep(delay)  # Attendre avant de réessayer
            else:
                print("Délai d'attente expiré après plusieurs tentatives")

def main():
    # Demander à l'utilisateur d'entrer un nom de domaine
    domain_name = input("Entrez un nom de domaine (par exemple, google.com) : ")
    
    # Obtenir et afficher les informations du domaine
    get_domain_info(domain_name)

if __name__ == "__main__":
    main()
