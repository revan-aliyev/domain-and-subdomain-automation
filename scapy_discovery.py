from scapy.all import sr1, IP, UDP, DNS, DNSQR

# Domen və subdomenlərin siyahısı
main_domain = "google.com"
subdomains = ["www", "mail", "ftp", "admin", "shop", "test"]

print(f"'{main_domain}' üçün DNS sorğularının göndərilməsi...\n")

# Hər bir subdomen üçün DNS sorğusu göndəririk
for sub in subdomains:
    domain = f"{sub}.{main_domain}"
    query = sr1(IP(dst="8.8.8.8")/UDP()/DNS(rd=1, qd=DNSQR(qname=domain)), verbose=False, timeout=2)
    if query and query.haslayer(DNS):
        answer = query[DNS].an
        if answer:
            print(f"✅ {domain} -> IP: {answer.rdata}")
        else:
            print(f"❌ {domain} -> DNS qeydi tapılmadı.")
    else:
        print(f"❌ {domain} -> DNS cavabı yoxdur.")
