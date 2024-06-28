"""
Copyright © 02/29/2024, Maxime Gaucher MSI E Cybersecurity 2024
Version: 6.0
Project
"""

import subprocess
import re
import requests

# List of secure and insecure operating systems
SECURE_OS_VERSIONS = {
    "windows": ["windows 10", "windows 11"],
    "linux": ["ubuntu 20.04", "ubuntu 22.04", "debian 10", "debian 11", "rhel 8", "centos 8"],
    "macos": ["macos monterey", "macos ventura"],
}

INSECURE_OS_VERSIONS = {
    "windows": ["windows xp", "windows vista", "windows 7"],
    "linux": ["ubuntu 18.04", "ubuntu 16.04", "debian 9", "centos 7"],
    "macos": ["macos mojave", "macos high sierra"],
}

# Function to execute an nmap scan with OS detection
def scan_os(ip_address):
    nmap_command = ["nmap", "-O", ip_address]
    result = subprocess.run(nmap_command, capture_output=True, text=True)

    if result.returncode != 0:
        raise Exception(f"Error executing nmap: {result.stderr}")

    return result.stdout

# Function to extract details about detected operating systems
def parse_nmap_os_output(nmap_output):
    os_info = []

    lines = nmap_output.split("\n")
    
    for line in lines:
        match = re.search(r"Running: (.+)", line)
        if match:
            os_description = match.group(1)
            os_info.append({"os": os_description})

    return os_info

# Function to check if operating system versions are secure
def check_os_versions(os_info):
    insecure_os = []

    for info in os_info:
        os_description = info["os"].lower()

        found_secure = False
        found_insecure = False

        for key, versions in SECURE_OS_VERSIONS.items():
            if any(secure in os_description for secure in versions):
                found_secure = True

        for key, versions in INSECURE_OS_VERSIONS.items():
            if any(insecure in os_description for insecure in versions):
                found_insecure = True

        if found_insecure and not found_secure:
            insecure_os.append(info)

    return insecure_os

# Function to search for exploits related to the OS
def search_exploits(os_description):
    query = f"{os_description} exploit vuln"
    url = f"https://www.exploit-db.com/search?q={requests.utils.quote(query)}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        if "No results found." in response.text:
            return "No known exploits found for this OS."
        
        return response.text  # In a real scenario, parse the response to get relevant details
    except requests.RequestException as e:
        return f"Error retrieving exploits: {e}"

# Main function to scan and analyze operating systems
def scan_and_analyze_os(target_ip):
    try:
        nmap_output = scan_os(target_ip)
        os_info = parse_nmap_os_output(nmap_output)
        
        if os_info:
            print()
            print(f"------------------------------------------------------------------")
            print("Detected Operating System Information:")
            for info in os_info:
                print(f"Operating System: {info['os']} ")

            insecure_os = check_os_versions(os_info)
            if insecure_os:
                print("\nInsecure Operating Systems Detected:")
                for os in insecure_os:
                    print(f"Operating System: {os['os']}")
                    exploits_info = search_exploits(os['os'])
                    print(f"Known Exploits: {exploits_info}")
            else:
                print("\nAll operating systems appear to be secure.")
        else:
            print("No operating system information detected.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print(f"------------------------------------------------------------------")

# Example usage
if __name__ == "__main__":
    target_ip = input("Enter the IP address to scan: ")
    scan_and_analyze_os(target_ip)
