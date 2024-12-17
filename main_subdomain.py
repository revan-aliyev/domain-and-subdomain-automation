import sublist3r

domain = "microsoft.com"
# "engines" parametrini vergüllə ayrılmış sətir kimi verin
engines = "baidu,google,bing,ask,netcraft,ssl,passivedns"

subdomains = sublist3r.main(domain, 40, savefile=None, ports=None, silent=False, verbose=True, enable_bruteforce=False, engines=engines)

print("Tapılan subdomenlər:")
for subdomain in subdomains:
    print(subdomain)
