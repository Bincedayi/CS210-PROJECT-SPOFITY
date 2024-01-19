import json
import matplotlib.pyplot as plt
from collections import defaultdict
from dateutil.parser import parse as parse_date

# Load data
with open(r"C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data\PROJEDEN KULLNACAGIM DATA\updated_unique_songs_detayli_formatted.json", encoding='utf-8') as file:
    songs_data = json.load(file)

# Aggregate liveness by month
monthly_valence = defaultdict(list)
for song in songs_data:
    if 'endTime' in song and 'valence' in song:
        month = parse_date(song['endTime']).strftime('%Y-%m')
        monthly_valence[month].append(song['valence'])

# Calculate average liveness per month
average_valence_per_month = {month: sum(valence) / len(valence)
                              for month, valence in monthly_valence.items()}

# Sort and plot
sorted_months = sorted(average_valence_per_month.keys())
sorted_liveness = [average_valence_per_month[month] for month in sorted_months]

plt.figure(figsize=(12, 6))
plt.plot(sorted_months, sorted_liveness, marker='o', color='blue')
plt.xlabel('Month')
plt.ylabel('Average valence')
plt.title('Average valence Per Month')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
