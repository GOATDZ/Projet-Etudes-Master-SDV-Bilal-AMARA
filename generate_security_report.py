import os
import subprocess
from fpdf import FPDF, XPos, YPos
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import requests
import whois
import nmap

class PDF(FPDF):
    def header(self):
        self.set_font('DejaVu', 'B', 12)
        self.cell(0, 10, 'Security Scan Report', border=False, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('DejaVu', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', border=False, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)

    def chapter_title(self, title):
        self.set_font('DejaVu', 'B', 12)
        self.cell(0, 10, title, border=False, align='L', new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('DejaVu', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def scan_ports(ip_address):
    nm = nmap.PortScanner()
    nm.scan(ip_address, '1-1024')
    return nm

def get_domain_info(domain_name):
    domain_info = whois.whois(domain_name)
    info = {
        "domain_name": domain_info.domain_name,
        "registrar": domain_info.registrar,
        "creation_date": domain_info.creation_date,
        "expiration_date": domain_info.expiration_date,
        "name_servers": domain_info.name_servers,
        "status": domain_info.status,
        "emails": domain_info.emails,
        "org": domain_info.org,
        "country": domain_info.country,
        "city": domain_info.city,
        "address": domain_info.address,
        "zipcode": domain_info.zipcode
    }
    return info

def scan_services(ip_address):
    nmap_command = ["nmap", "-sV", "--script=vuln", ip_address]
    result = subprocess.run(nmap_command, capture_output=True, text=True)
    return result.stdout

def scan_os(ip_address):
    nmap_command = ["nmap", "-O", ip_address]
    result = subprocess.run(nmap_command, capture_output=True, text=True)
    return result.stdout

def generate_html_report(ip_address, domain_info, port_scan_results, service_scan_results, os_scan_results):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('report_template.html')
    output_html = template.render(
        ip_address=ip_address,
        domain_info=domain_info,
        port_scan_results=port_scan_results,
        service_scan_results=service_scan_results,
        os_scan_results=os_scan_results,
        date=datetime.now().strftime('%Y-%m-%d %H:%M')
    )
    with open("Report_Security.html", "w") as f:
        f.write(output_html)
    print("HTML report generated successfully.")

def format_port_scan_results(nm):
    results = ""
    for host in nm.all_hosts():
        results += f"Host: {host}\n"
        for proto in nm[host].all_protocols():
            results += f"Protocol: {proto}\n"
            ports = nm[host][proto].keys()
            for port in ports:
                results += f"Port: {port}\tState: {nm[host][proto][port]['state']}\n"
    return results

def generate_pdf_report(ip_address, domain_info, port_scan_results, service_scan_results, os_scan_results):
    pdf = PDF()

    # Add DejaVu font
    font_dir = 'dejavu-fonts-ttf-2.37/ttf'
    pdf.add_font('DejaVu', '', os.path.join(font_dir, 'DejaVuSans.ttf'), uni=True)
    pdf.add_font('DejaVu', 'B', os.path.join(font_dir, 'DejaVuSans-Bold.ttf'), uni=True)
    pdf.add_font('DejaVu', 'I', os.path.join(font_dir, 'DejaVuSans-Oblique.ttf'), uni=True)
    
    pdf.add_page()

    pdf.set_font("DejaVu", size=16)
    pdf.cell(200, 10, txt="Scan Report", border=False, align='C')

    pdf.set_font("DejaVu", size=12)
    pdf.cell(200, 10, txt=f"Date: {datetime.now().strftime('%B %d, %Y')}", border=False, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.ln(10)

    pdf.chapter_title("Summary")
    summary_text = (
        f"This document reports on the results of an automatic security scan.\n\n"
        f"IP Address: {ip_address}\n"
        f"Domain Information: {domain_info}\n"
    )
    pdf.chapter_body(summary_text)

    pdf.chapter_title("1. Port Scan Results")
    pdf.chapter_body(port_scan_results)

    pdf.chapter_title("2. Service Scan Results")
    pdf.chapter_body(service_scan_results)

    pdf.chapter_title("3. OS Scan Results")
    pdf.chapter_body(os_scan_results)

    report_filename = f"Report_Security_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.pdf"
    pdf.output(report_filename)
    print(f"PDF report generated successfully: {report_filename}")

def main():
    ip_address = input("Enter the IP address for the security report: ")
    domain_name = input("Enter the domain name for the security report: ")

    domain_info = get_domain_info(domain_name)

    nm = scan_ports(ip_address)
    port_scan_results = format_port_scan_results(nm)
    service_scan_results = scan_services(ip_address)
    os_scan_results = scan_os(ip_address)

    report_format = input("Enter the report format (pdf or html): ").strip().lower()
    if report_format == "html":
        generate_html_report(ip_address, domain_info, port_scan_results, service_scan_results, os_scan_results)
    elif report_format == "pdf":
        generate_pdf_report(ip_address, domain_info, port_scan_results, service_scan_results, os_scan_results)
    else:
        print("Invalid format. Please enter 'pdf' or 'html'.")

if __name__ == "__main__":
    main()
