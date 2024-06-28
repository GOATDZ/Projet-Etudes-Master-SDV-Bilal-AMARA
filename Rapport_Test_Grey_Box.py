import nmap
import socket
import subprocess
from fpdf import FPDF

# Fonction pour scanner les ports et services ouverts
def scan_ports(ip):
    nm = nmap.PortScanner()  # Initialisation du scanner Nmap
    nm.scan(ip, arguments='-sV')  # Scan de l'adresse IP avec détection de version des services
    scan_data = []  # Liste pour stocker les résultats du scan
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()  # Liste des ports
            for port in lport:
                service = nm[host][proto][port]
                scan_data.append({
                    'port': port,
                    'name': service['name'],
                    'product': service.get('product', 'unknown'),
                    'version': service.get('version', 'unknown')
                })
    return scan_data

# Fonction pour obtenir des informations sur l'OS
def scan_os(ip):
    nm = nmap.PortScanner()  # Initialisation du scanner Nmap
    nm.scan(ip, arguments='-O')  # Scan pour détecter l'OS
    os_data = nm[ip]['osclass'] if 'osclass' in nm[ip] else []
    return os_data

# Fonction pour obtenir le nom de domaine associé à une adresse IP
def get_domain(ip):
    try:
        domain = socket.gethostbyaddr(ip)
        return domain[0]  # Retourne le nom de domaine
    except socket.herror:
        return None  # Aucun nom de domaine trouvé

# Fonction pour rechercher des exploits liés aux services
def search_exploits(service_name, service_version):
    exploits = []
    searchsploit_path = "searchsploit"  # Assure que searchsploit est dans le PATH
    command = f"{searchsploit_path} {service_name} {service_version}"  # Commande à exécuter
    result = subprocess.run(command.split(), capture_output=True, text=True)  # Exécution de la commande
    if result.returncode == 0:
        for line in result.stdout.split('\n'):
            if "|" in line:
                exploits.append(line.strip())  # Ajout des exploits trouvés à la liste
    return exploits

# Fonction pour générer un rapport PDF
def generate_pdf(ip, os_data, scan_data, domain, exploits):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Titre du rapport
    pdf.cell(200, 10, txt="Rapport de Scan IP", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Adresse IP: {ip}", ln=True)
    
    # Nom de domaine
    if domain:
        pdf.cell(200, 10, txt=f"Nom de domaine: {domain}", ln=True)
    
    # Informations sur l'OS
    pdf.cell(200, 10, txt="Informations sur l'OS:", ln=True)
    for os in os_data:
        pdf.cell(200, 10, txt=f"OS: {os['osfamily']} - {os['osgen']} - {os['accuracy']}%", ln=True)

    # Informations sur les ports et services ouverts
    pdf.cell(200, 10, txt="Ports et services ouverts:", ln=True)
    for data in scan_data:
        pdf.cell(200, 10, txt=f"Port: {data['port']} - Service: {data['name']} - Produit: {data['product']} - Version: {data['version']}", ln=True)

    # Informations sur les exploits trouvés
    pdf.cell(200, 10, txt="Exploits trouvés:", ln=True)
    for exploit in exploits:
        pdf.cell(200, 10, txt=exploit, ln=True)

    # Sauvegarde du fichier PDF
    pdf.output(f"rapport_{ip}.pdf")

# Fonction principale
def main(ip):
    scan_data = scan_ports(ip)  # Scan des ports et services
    os_data = scan_os(ip)  # Scan des informations sur l'OS
    domain = get_domain(ip)  # Obtention du nom de domaine
    all_exploits = []
    for service in scan_data:
        exploits = search_exploits(service['name'], service['version'])  # Recherche d'exploits
        all_exploits.extend(exploits)
    generate_pdf(ip, os_data, scan_data, domain, all_exploits)  # Génération du rapport PDF

if __name__ == "__main__":
    ip_address = input("Entrez l'adresse IP à scanner: ")  # Saisie de l'adresse IP par l'utilisateur
    main(ip_address)  # Exécution de la fonction principale
