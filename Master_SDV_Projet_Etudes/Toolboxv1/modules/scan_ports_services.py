import socket
import nmap
from scapy.all import ARP, Ether, srp
import json
import csv
import geoip2.database
import requests
import ipaddress

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        public_ip = response.json()['ip']
        return public_ip
    except Exception as e:
        return {'error': str(e)}

def scan_ports(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024')

    scan_data = {}
    for host in nm.all_hosts():
        scan_data[host] = {
            'hostnames': nm[host].hostnames(),
            'state': nm[host].state(),
            'protocols': {}
        }
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            scan_data[host]['protocols'][proto] = {}
            for port in lport:
                scan_data[host]['protocols'][proto][port] = {
                    'state': nm[host][proto][port]['state'],
                    'name': nm[host][proto][port]['name'],
                    'product': nm[host][proto][port]['product'],
                    'version': nm[host][proto][port]['version'],
                    'extrainfo': nm[host][proto][port]['extrainfo'],
                }
    return scan_data

def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def is_private_ip(ip):
    return ipaddress.ip_address(ip).is_private

def get_geoip_info(ip):
    if is_private_ip(ip):
        ip = get_public_ip()
        if 'error' in ip:
            return ip

    try:
        reader = geoip2.database.Reader('GeoLite2-City.mmdb')
        response = reader.city(ip)
        return {
            'city': response.city.name,
            'country': response.country.name,
            'latitude': response.location.latitude,
            'longitude': response.location.longitude
        }
    except Exception as e:
        return {'error': str(e)}

def export_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def export_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['host', 'hostname', 'state', 'protocol', 'port', 'name', 'product', 'version', 'extrainfo', 'city', 'country', 'latitude', 'longitude']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for host, host_data in data.items():
            geoip_info = get_geoip_info(host)
            for proto, ports in host_data['protocols'].items():
                for port, port_data in ports.items():
                    writer.writerow({
                        'host': host,
                        'hostname': host_data['hostnames'],
                        'state': host_data['state'],
                        'protocol': proto,
                        'port': port,
                        'name': port_data['name'],
                        'product': port_data['product'],
                        'version': port_data['version'],
                        'extrainfo': port_data['extrainfo'],
                        'city': geoip_info.get('city', ''),
                        'country': geoip_info.get('country', ''),
                        'latitude': geoip_info.get('latitude', ''),
                        'longitude': geoip_info.get('longitude', '')
                    })

def main():
    target_ip = input("Entrez l'adresse IP ou le domaine à scanner: ")
    print("Scan des ports...")
    ports_data = scan_ports(target_ip)
    print("Résultat du scan des ports :")
    for host, data in ports_data.items():
        print(f"Host : {host}")
        print(f"Hostnames : {data['hostnames']}")
        print(f"State : {data['state']}")
        for proto, ports in data['protocols'].items():
            print(f"Protocol : {proto}")
            for port, port_data in ports.items():
                print(f"Port : {port}")
                for key, value in port_data.items():
                    print(f"  {key} : {value}")
        geoip_info = get_geoip_info(host)
        print(f"GeoIP : {geoip_info}")
        print()

    ip_range = input("Entrez la plage d'adresses IP pour scanner le réseau (e.g., 192.168.1.0/24) : ")
    print("Scan du réseau...")
    devices = scan_network(ip_range)
    print("Résultat du scan du réseau :")
    for device in devices:
        print(f"IP : {device['ip']}    MAC : {device['mac']}")

    export_choice = input("Voulez-vous exporter les résultats ? (json/csv/none) : ")
    if export_choice.lower() == 'json':
        filename = input("Entrez le nom du fichier pour l'exportation JSON : ")
        export_to_json(ports_data, filename)
        print(f"Résultats exportés vers {filename}")
    elif export_choice.lower() == 'csv':
        filename = input("Entrez le nom du fichier pour l'exportation CSV : ")
        export_to_csv(ports_data, filename)
        print(f"Résultats exportés vers {filename}")

if __name__ == "__main__":
    main()
