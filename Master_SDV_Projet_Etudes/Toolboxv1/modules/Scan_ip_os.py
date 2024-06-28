import nmap
import platform
import subprocess
import socket
from macvendors import get_vendor_from_mac  # Importer la fonction get_vendor_from_mac depuis macvendors.py
from MAC import get_mac_address  # Importer la fonction get_mac_address depuis MAC.py

def get_domain_name(ip_address):
    try:
        # Utilisation de socket.gethostbyaddr pour obtenir le nom de domaine associé à l'adresse IP
        domain_name = socket.gethostbyaddr(ip_address)[0]
        return domain_name
    except Exception as e:
        print(f"Error retrieving domain name for IP {ip_address}: {e}")
        return "Domain name not found"

def extract_dns_parts(domain_name):
    try:
        parts = domain_name.split('.')
        if len(parts) >= 2:
            suffix = parts[-1]
            prefix = parts[0]
            radical = '.'.join(parts[1:-1]) if len(parts) > 2 else ''
        else:
            suffix = ''
            prefix = parts[0] if parts else ''
            radical = ''
        return prefix, radical, suffix
    except Exception as e:
        print(f"Error extracting DNS parts from domain name {domain_name}: {e}")
        return "Prefix not found", "Radical not found", "Suffix not found"

def scan_ip_os(target):
    nm = nmap.PortScanner()

    # Options de scan
    scan_options = '-O -sS'
    if platform.system() == 'Linux':
        scan_options += ' -Pn'  # Ajouter -Pn si le système est Linux pour ignorer les sondes de ping

    # Entête du scan
    print(f"Initiating scan for target: {target}\n")

    # Scan de l'adresse IP cible avec les options correctes
    nm.scan(target, arguments=scan_options)

    # Récupération des informations sur l'adresse IP cible
    for host in nm.all_hosts():
        print(f"{'='*20} Host Information {'='*20}")
        print(f"Target Host: {host}")
        print()

        # Informations sur le système d'exploitation
        if 'osmatch' in nm[host]:
            print("Operating System Information:")
            for osmatch in nm[host]['osmatch']:
                print(f"  - Name: {osmatch['name']}")
                print(f"  - Accuracy: {osmatch['accuracy']}%")
            print()
        else:
            print("Operating System: Not identified\n")

        # Récupération de l'adresse MAC à partir de l'adresse IP
        try:
            mac_address = get_mac_address(host)
            if mac_address == "MAC address not found":
                print(f"MAC Address: {mac_address}")
            else:
                print(f"MAC Address: {mac_address}")

                # Obtention du vendor à partir de l'adresse MAC
                vendor = get_vendor_from_mac(mac_address)
                print(f"Vendor: {vendor}\n")

        except Exception as e:
            print(f"Error retrieving MAC address for {host}: {e}\n")

        # Adresses IP et noms de domaine associés
        if 'addresses' in nm[host]:
            ip_addresses = nm[host]['addresses'].values()
            print(f"IP Address(es): {', '.join(ip_addresses)}")
            for ip_address in ip_addresses:
                domain_name = get_domain_name(ip_address)
                print(f"Domain Name: {domain_name}")
                prefix, radical, suffix = extract_dns_parts(domain_name)
                print(f"  - Prefix: {prefix}")
                print(f"  - Radical: {radical}")
                print(f"  - Suffix: {suffix}")
            print()

    # Récupération des informations sur la machine locale
    print(f"{'='*20} Local Machine Information {'='*20}")
    print(f"- Hostname: {platform.node()}")
    print(f"- IP Address: {subprocess.getoutput('hostname -I').split()[0]}")
    print(f"- System: {platform.system()} {platform.release()} {platform.architecture()[0]}")

if __name__ == "__main__":
    target = input("Enter the target IP or network range: ")
    scan_ip_os(target)
