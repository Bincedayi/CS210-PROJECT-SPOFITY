import json
import matplotlib.pyplot as plt
from collections import defaultdict
from dateutil.parser import parse as parse_date

# Load the updated detailed JSON file
with open(r"C:\Users\\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data\PROJEDEN KULLNACAGIM DATA\updated_unique_songs_detayli_formatted.json", encoding='utf-8') as file:
    songs_data = json.load(file)

# Aggregate instrumentalness by month
monthly_instrumentalness = defaultdict(list)
for song in songs_data:
    if 'endTime' in song and 'instrumentalness' in song:
        month = parse_date(song['endTime']).strftime('%Y-%m')
        monthly_instrumentalness[month].append(song['instrumentalness'])

# Calculate average instrumentalness per month
average_instrumentalness_per_month = {month: sum(instrumentalness) / len(instrumentalness)
                                      for month, instrumentalness in monthly_instrumentalness.items()}

# Sort the data by month
sorted_months_instrumentalness = sorted(average_instrumentalness_per_month.keys())
sorted_instrumentalness = [average_instrumentalness_per_month[month] for month in sorted_months_instrumentalness]

# Plotting for Instrumentalness
plt.figure(figsize=(12, 6))
plt.plot(sorted_months_instrumentalness, sorted_instrumentalness, marker='o', color='magenta')
plt.xlabel('Month')
plt.ylabel('Average Instrumentalness')
plt.title('Average Instrumentalness Per Month')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
