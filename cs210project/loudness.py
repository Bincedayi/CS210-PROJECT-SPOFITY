import json
import matplotlib.pyplot as plt
from collections import defaultdict
from dateutil.parser import parse as parse_date

# Load the updated detailed JSON file
with open(r"C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data\PROJEDEN KULLNACAGIM DATA\updated_unique_songs_detayli_formatted.json", encoding='utf-8') as file:
    songs_data = json.load(file)

# Aggregate loudness by month
monthly_loudness = defaultdict(list)
for song in songs_data:
    if 'endTime' in song and 'loudness' in song:
        month = parse_date(song['endTime']).strftime('%Y-%m')
        monthly_loudness[month].append(song['loudness'])

# Calculate average loudness per month
average_loudness_per_month = {month: sum(loudness) / len(loudness)
                              for month, loudness in monthly_loudness.items()}

# Sort the data by month
sorted_months_loudness = sorted(average_loudness_per_month.keys())
sorted_loudness = [average_loudness_per_month[month] for month in sorted_months_loudness]

# Plotting for Loudness
plt.figure(figsize=(12, 6))
plt.plot(sorted_months_loudness, sorted_loudness, marker='o', color='red')
plt.xlabel('Month')
plt.ylabel('Average Loudness (dB)')
plt.title('Average Loudness Per Month')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
