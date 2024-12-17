import httpx

# Subdomenlər üçün siyahı
subdomains = ["www", "mail", "ftp", "admin", "shop", "test"]
main_domain = "microsoft.com"

print(f"'{main_domain}' üçün HTTP/HTTPS status kodlarının yoxlanması başlanır...\n")

# Aktiv subdomenləri yoxlamaq
for sub in subdomains:
    url = f"http://{sub}.{main_domain}"
    try:
        response = httpx.get(url, timeout=10)
        print(f"✅ {url} -> Status: {response.status_code}")
    except httpx.ConnectTimeout:
        print(f"⚠️ {url} -> Bağlantı zamanı aşdı (Timeout).")
    except httpx.ConnectError:
        print(f"❌ {url} -> Bağlantı mümkün deyil.")
    except Exception as e:
        print(f"⚠️ {url} -> Naməlum xəta: {e}")
