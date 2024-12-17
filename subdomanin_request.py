import requests

def check_subdomain(domain, subdomains):
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f"[LIVE] {url}")
            else:
                print(f"[NOT LIVE] {url} - Status Code: {response.status_code}")
        except requests.exceptions.RequestException:
            print(f"[ERROR] Could not connect to {url}")

# Subdomain sözlüyü
subdomain_list = ["www", "mail", "blog", "shop", "api", "ftp"]

# Domen adı
domain_name = "google.com"

# Test
check_subdomain(domain_name, subdomain_list)
