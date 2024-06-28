from scapy.all import srp, Ether, ARP

def get_mac_address(ip_address):
    try:
        arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_address)
        answered, unanswered = srp(arp_request, timeout=2, verbose=False)
        
        for pkt in answered:
            mac_address = pkt[1].src.upper()  # Convertir en majuscules
            return mac_address
        
        return "MAC address not found"
    except Exception as e:
        print(f"Error retrieving MAC address for IP {ip_address}: {e}")
        return "Error"

if __name__ == "__main__":
    ip_address = input("Enter the IP address: ")
    mac_address = get_mac_address(ip_address)
    print(f"MAC Address for {ip_address}: {mac_address}")
