import requests

def get_vendor_from_mac(mac_address):
    try:
        # Formatage de l'adresse MAC pour le requête API
        mac_address = mac_address.upper().replace(':', '')

        # URL de l'API de macvendors.com
        url = f"https://api.macvendors.com/{mac_address}"

        # Faire la requête GET à l'API
        response = requests.get(url)

        # Vérification du statut de la réponse
        if response.status_code == 200:
            return response.text.strip()
        else:
            return f"Vendor not found (Status Code: {response.status_code})"

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving vendor information: {e}")
        return "Vendor error"
