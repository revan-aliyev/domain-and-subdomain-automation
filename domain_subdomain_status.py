import requests

# Subdomenlərin siyahısı
subdomain_list = ["www", "mail", "blog", "shop", "api", "ftp"]

# Domenləri fayldan oxuyan funksiya
def read_domains(file_name):
    try:
        with open(file_name, 'r') as file:
            domains = file.readlines()
        return [domain.strip() for domain in domains]
    except FileNotFoundError:
        print(f"Fayl tapılmadı: {file_name}")
        return []

# Subdomenləri yoxlayan funksiya
def check_subdomains(domain, subdomain_list):
    results = []
    for subdomain in subdomain_list:
        url = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(url, timeout=5)  
            results.append((f"{subdomain}.{domain}", response.status_code))
        except requests.exceptions.RequestException as e:
            results.append((f"{subdomain}.{domain}", "Error"))
    return results

# Nəticəni fayla yazan funksiya
def write_results(file_name, results):
    with open(file_name, 'w') as file:
        for subdomain, status in results:
            file.write(f"{subdomain}: {status}\n")

def main():
    # Domenləri oxuyuruq
    domains = read_domains("input.txt")
    if not domains:
        return
    
    all_results = []
    # Hər bir domen üçün subdomenləri yoxlayırıq
    for domain in domains:
        print(f"Checking subdomains for {domain}...")
        results = check_subdomains(domain, subdomain_list)
        all_results.extend(results)
    
    # Nəticəni fayla yazırıq
    write_results("output.txt", all_results)
    print("Nəticələr output.txt faylına yazıldı.")

if __name__ == "__main__":
    main()
