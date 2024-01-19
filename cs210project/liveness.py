import json
import matplotlib.pyplot as plt
from collections import defaultdict
from dateutil.parser import parse as parse_date

# Load data
with open(r"C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data\PROJEDEN KULLNACAGIM DATA\updated_unique_songs_detayli_formatted.json", encoding='utf-8') as file:
    songs_data = json.load(file)

# Aggregate liveness by month
monthly_liveness = defaultdict(list)
for song in songs_data:
    if 'endTime' in song and 'liveness' in song:
        month = parse_date(song['endTime']).strftime('%Y-%m')
        monthly_liveness[month].append(song['liveness'])

# Calculate average liveness per month
average_liveness_per_month = {month: sum(liveness) / len(liveness)
                              for month, liveness in monthly_liveness.items()}

# Sort and plot
sorted_months = sorted(average_liveness_per_month.keys())
sorted_liveness = [average_liveness_per_month[month] for month in sorted_months]

plt.figure(figsize=(12, 6))
plt.plot(sorted_months, sorted_liveness, marker='o', color='blue')
plt.xlabel('Month')
plt.ylabel('Average Liveness')
plt.title('Average Liveness Per Month')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
