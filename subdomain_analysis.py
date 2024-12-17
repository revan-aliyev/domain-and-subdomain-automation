import socket
import requests
import argparse

# Subdomenlərin siyahısı
subdomain_list = ["www", "mail", "blog", "shop", "api", "ftp", "dev", "test"]

def find_subdomains(domain, subdomains):
    results = []
    for subdomain in subdomains:
        full_domain = f"{subdomain}.{domain}"
        try:
            ip_address = socket.gethostbyname(full_domain)
            print(f"[FOUND] {full_domain} -> {ip_address}")
            results.append((full_domain, ip_address))
        except socket.gaierror:
            print(f"[NOT FOUND] {full_domain}")
            results.append((full_domain, None))
    return results

def check_http_status(domains):
    output = []
    for domain, ip in domains:
        if ip:
            try:
                response = requests.get(f"http://{domain}", timeout=5)
                print(f"[HTTP] {domain} -> {response.status_code}")
                output.append((domain, ip, response.status_code))
            except requests.exceptions.RequestException as e:
                print(f"[ERROR] {domain}: {e}")
                output.append((domain, ip, "Error"))
        else:
            output.append((domain, "No IP", "Not Resolved"))
    return output

def save_results_to_file(results, txt_filename="output.txt"):
    # Nəticələri fayla yaz
    with open(txt_filename, "w") as txt_file:
        for domain, ip, status in results:
            txt_file.write(f"{domain} ({ip}) -> {status}\n")
    print(f"Results saved to {txt_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain Enumeration Tool")
    parser.add_argument("domain", help="Target domain for subdomain enumeration")
    args = parser.parse_args()

    # Domeni parametr olaraq al
    domain_name = args.domain

    # Subdomenləri yoxla
    subdomain_results = find_subdomains(domain_name, subdomain_list)

    # HTTP status kodlarını yoxla
    http_results = check_http_status(subdomain_results)

    # Nəticələri fayla yaz
    save_results_to_file(http_results)
