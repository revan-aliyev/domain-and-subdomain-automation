import socket

def find_subdomains(domain, subdomains):
    for subdomain in subdomains:
        full_domain = f"{subdomain}.{domain}"
        try:
            ip_address = socket.gethostbyname(full_domain)
            print(f"[FOUND] {full_domain} -> {ip_address}")
        except socket.gaierror:
            print(f"[NOT FOUND] {full_domain}")

# Subdomain siyahısı
subdomain_list = ["www", "mail", "blog", "api", "dev", "test"]

# Domen adı
domain_name = "microsoft.com"

# Test
find_subdomains(domain_name, subdomain_list)
