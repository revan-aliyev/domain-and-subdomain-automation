import argparse
import socket

# Komanda sətirindən domenləri almaq üçün argparse istifadə edirik
def get_command_line_args():
    parser = argparse.ArgumentParser(description="Domen adlarının IP ünvanlarını tapmaq")
    parser.add_argument("domains", metavar="D", type=str, help="Domen adlarını vergüllə ayrılmış şəkildə daxil edin")
    args = parser.parse_args()
    return args.domains.split(',')

# Domen adının IP ünvanını tapırıq
def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return f"Error: {domain} ünvanı tapılmadı."

def main():
    # Komanda sətirindən domenləri alırıq
    domains = get_command_line_args()

    # Hər domen üçün IP ünvanını tapırıq və nəticələri göstəririk
    with open("output.txt", "w") as output_file:
        for domain in domains:
            ip = get_ip_address(domain)
            output_file.write(f"IP address for {domain}: {ip}\n")
            print(f"IP address for {domain}: {ip}")

if __name__ == "__main__":
    main()
