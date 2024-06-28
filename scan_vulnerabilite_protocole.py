import subprocess
import re
import requests

# Function to execute an nmap scan with service and version detection
def scan_services(ip_address):
    nmap_command = ["nmap", "-sV", "--script=vuln", ip_address]
    result = subprocess.run(nmap_command, capture_output=True, text=True)

    if result.returncode != 0:
        raise Exception(f"Error executing nmap: {result.stderr}")

    return result.stdout

# Function to parse nmap output for services and vulnerabilities
def parse_nmap_output(nmap_output):
    services = []
    vulnerabilities = []

    lines = nmap_output.split("\n")
    service_pattern = re.compile(r"(\d{1,5}/\w+)\s+open\s+([\w\-]+)\s+([\w\.\-]+)")
    vuln_pattern = re.compile(r"\|\s+([\w\s\-]+):\s*(.*)")

    current_service = None

    for line in lines:
        service_match = service_pattern.search(line)
        if service_match:
            port_protocol = service_match.group(1)
            service_name = service_match.group(2)
            service_version = service_match.group(3)
            current_service = {
                "port_protocol": port_protocol,
                "service_name": service_name,
                "service_version": service_version,
                "vulnerabilities": []
            }
            services.append(current_service)
            continue

        if current_service:
            vuln_match = vuln_pattern.search(line)
            if vuln_match:
                vuln_name = vuln_match.group(1).strip()
                vuln_info = vuln_match.group(2).strip()
                current_service["vulnerabilities"].append({
                    "name": vuln_name,
                    "info": vuln_info
                })
                vulnerabilities.append({
                    "service": current_service,
                    "name": vuln_name,
                    "info": vuln_info
                })

    return services, vulnerabilities

# Function to display scan results
def display_results(services, vulnerabilities):
    print(f"\n{'-'*66}")
    print(f"Detected Services and Vulnerabilities")
    print(f"{'-'*66}\n")
    for service in services:
        print(f"Service: {service['service_name']} {service['service_version']} ({service['port_protocol']})")
        if service["vulnerabilities"]:
            print(f"Vulnerabilities:")
            for vuln in service["vulnerabilities"]:
                print(f"  - {vuln['name']}: {vuln['info']}")
        else:
            print("  No known vulnerabilities found.")
        print(f"{'-'*66}\n")

# Main function to scan and analyze services and vulnerabilities
def scan_and_analyze_vulnerabilities(target_ip):
    try:
        nmap_output = scan_services(target_ip)
        services, vulnerabilities = parse_nmap_output(nmap_output)
        display_results(services, vulnerabilities)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    target_ip = input("Enter the IP address to scan: ")
    scan_and_analyze_vulnerabilities(target_ip)
