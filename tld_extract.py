import tldextract

# URL-lərin siyahısı
urls = [
    "https://mail.onedrive.com",
    "https://shop.onedrive.com",
    "https://admin.test.onedrive.com"
]

print("URL-lərdən əsas domen, subdomen və TLD-nin ayırd edilməsi:\n")

# Hər URL üçün domen məlumatlarını ayırmaq
for url in urls:
    extracted = tldextract.extract(url)
    print(f"URL: {url}")
    print(f"  Subdomen: {extracted.subdomain}")
    print(f"  Əsas Domen: {extracted.domain}")
    print(f"  TLD: {extracted.suffix}\n")
