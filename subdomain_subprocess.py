import subprocess

def run_sublist3r(domain):
    try:
        subprocess.run(["sublist3r", "-d", domain, "-o", "subdomains.txt"])
        print(f"Subdomains saved to subdomains.txt")
    except Exception as e:
        print(f"Error running Sublist3r: {e}")

# Test
run_sublist3r("microsoft.com")
