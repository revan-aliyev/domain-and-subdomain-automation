import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Daha çox domen və IP ünvanları ilə məlumatlar
data = {
    "Domen": [
        "diziwatch.net", "diziwatch.net", "diziwatch.net",
        "example.com", "example.com", "example.com",
        "google.com", "google.com", "google.com",
        "youtube.com", "youtube.com", "youtube.com",
        "facebook.com", "facebook.com", "facebook.com"
    ],
    "Tarix": [
        "2024-01-01", "2024-01-02", "2024-01-03",
        "2024-01-01", "2024-01-02", "2024-01-03",
        "2024-01-01", "2024-01-02", "2024-01-03",
        "2024-01-01", "2024-01-02", "2024-01-03",
        "2024-01-01", "2024-01-02", "2024-01-03"
    ],
    "IP_Count": [1, 2, 1, 2, 1, 3, 3, 4, 2, 1, 2, 2, 4, 5, 3]
}

# Verilənləri DataFrame-ə çeviririk
df = pd.DataFrame(data)

# Tarixi datetime tipinə çeviririk
df['Tarix'] = pd.to_datetime(df['Tarix'])

# Domenlər və tarixlər üzrə qruplaşdırırıq və IP ünvanlarının sayını hesablayırıq
grouped = df.pivot_table(index='Tarix', columns='Domen', values='IP_Count', aggfunc='sum')

# Qruplaşdırılmış bar qrafiki
fig, ax = plt.subplots(figsize=(10, 6))

# Bar qrafikini çəkmək
grouped.plot(kind='bar', ax=ax)

# Qrafikin başlığını və oxları təyin edirik
plt.title('Domenlər üzrə IP Ünvanlarının Sayı (Tarixə görə)')
plt.xlabel('Tarix')
plt.ylabel('IP Ünvanlarının Sayı')

# Qrafikdəki etiketləri yaxşı göstərmək üçün x oxunu döndürürük
plt.xticks(rotation=45)

# Qrafiki göstəririk
plt.tight_layout()
plt.show()
