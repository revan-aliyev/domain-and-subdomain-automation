import dns.resolver
import sys

# Fayla yazmaq üçün sys.stdout-u dəyişdiririk
sys.stdout = open('output.txt', 'w')

def get_a_record(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        for ipval in result:
            print(f"A record for {domain}: {ipval.to_text()}")
    except dns.resolver.NoAnswer:
        print(f"No A record found for {domain}")

# Test
get_a_record("diziwatch.net")
