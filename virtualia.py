import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
subdomains = ["microsoft.com", "mail.microsoft.com", "shop.microsoft.com", "api.microsoft.com", "test.microsoft.com", "blog.microsoft.com"]

for subdomain in subdomains:
    G.add_edge("root", subdomain)

nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()
