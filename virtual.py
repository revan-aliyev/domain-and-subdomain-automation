import networkx as nx
import matplotlib.pyplot as plt

# Şəbəkə yaratmaq
G = nx.Graph()

# Domenlər və IP ünvanları
data = {
    "www.diziwatch.net": "93.184.216.34",
    "blog.diziwatch.net": "93.184.216.34",
    "blog.google.com": "142.250.190.78",
    "api.google.com" : "142.250.190.78",
    "mail.microsoft.com": "199.59.243.277",
    "ftp.microsoft.com": "199.59.243.277",
    "dev.microsoft.com": "199.59.243.277",
    "test.microsoft.com": "199.59.243.277"
}

# Şəbəkəyə düyünlər əlavə edirik
for domain, ip in data.items():
    G.add_edge(domain, ip)

# Şəbəkə qrafikini çəkmək
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_size=3000, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray")
plt.title("Domenlər və Onların IP Ünvanları Arasında Əlaqə")
plt.show()
