import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Daha çox domen və IP ünvanları əlavə edirik
data = {
    "Domen": [
        "diziwatch.net", "example.com", "google.com", "youtube.com", "facebook.com",
        "twitter.com", "github.com", "yahoo.com", "linkedin.com", "wikipedia.org"
    ],
    "IP": [
        "93.184.216.34", "93.184.216.34", "142.250.190.78", "172.217.15.142", "31.13.71.36",
        "104.244.42.129", "140.82.121.3", "98.137.246.8", "108.174.10.10", "208.80.154.224"
    ]
}

df = pd.DataFrame(data)

# Domen və IP ünvanı arasındakı əlaqəni matris şəklində göstəririk
pivot = df.pivot_table(index="Domen", columns="IP", aggfunc="size", fill_value=0)

# Heatmap yaratmaq
plt.figure(figsize=(10, 8))
sns.heatmap(pivot, annot=True, cmap="Blues", fmt="d", linewidths=.5)
plt.title('Domenlər və IP Ünvanları Arasında Əlaqə - Heatmap')
plt.show()
