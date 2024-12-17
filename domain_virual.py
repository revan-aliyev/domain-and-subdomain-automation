import socket
import matplotlib.pyplot as plt
import pandas as pd

# input.txt faylından domenləri oxuyuruq
def get_domains_from_file(file_name):
    try:
        with open(file_name, 'r') as f:
            domains = f.readlines()
        return [domain.strip() for domain in domains]  
    except FileNotFoundError:
        print(f"{file_name} faylı tapılmadı!")
        return []

# Domenlərə aid IP ünvanlarını tapırıq
def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return "IP tapılmadı"

# input.txt faylından domenləri alırıq
domains = get_domains_from_file('input.txt')

# Domenlər və onların IP ünvanları
ips = [get_ip(domain) for domain in domains]

# Məlumatları DataFrame-ə yükləyirik
data = {
    "Domen": domains,
    "IP": ips
}

df = pd.DataFrame(data)

# Domenlərin sayı
domain_count = df["Domen"].count()

# Qrafik yaratmaq
plt.figure(figsize=(10, 6))
plt.bar(df["Domen"], df["IP"])
plt.title('Domenlər və IP Ünvanları')
plt.xlabel('Domen')
plt.ylabel('Dəyər')

plt.xticks(rotation=45, ha="right")  
plt.tight_layout()  
plt.show()