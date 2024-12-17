import socket

# input.txt faylından domenləri oxuyuruq
def get_domains_from_file(file_name):
    with open(file_name, 'r') as f:
        domains = f.readlines()
    return [domain.strip() for domain in domains]

# Domen adlarının IP ünvanlarını tapırıq
def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return f"Error resolving {domain}"

# Nəticələri output.txt faylına yazırıq
def write_output_to_file(results):
    with open('output.txt', 'w') as f:
        for result in results:
            f.write(result + '\n')

def main():
    # Domenləri input.txt faylından alırıq
    domains = get_domains_from_file('input.txt')
    
    results = []
    for domain in domains:
        ip_address = get_ip_address(domain)
        results.append(f"IP address for {domain}: {ip_address}")
    
    # Nəticələri output.txt faylına yazırıq
    write_output_to_file(results)
    print("Results written to output.txt")

if __name__ == '__main__':
    main()
