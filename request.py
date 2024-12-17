import requests

def check_subdomain(subdomain):
    url = f"https://{subdomain}"  
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{subdomain} is live.")
        else:
            print(f"{subdomain} responded with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {subdomain}: {e}")

subdomains = [
    "mail.google.com",
    "www.google.com",
    "drive.google.com",
    "calendar.google.com"
]

for subdomain in subdomains:
    check_subdomain(subdomain)
