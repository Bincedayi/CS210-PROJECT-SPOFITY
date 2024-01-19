import json
import matplotlib.pyplot as plt
from collections import defaultdict
from dateutil.parser import parse as parse_date

# Load the updated detailed JSON file
with open(r"C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data\PROJEDEN KULLNACAGIM DATA\updated_unique_songs_detayli_formatted.json", encoding='utf-8') as file:
    songs_data = json.load(file)

# Aggregate acousticness by month
monthly_acousticness = defaultdict(list)
for song in songs_data:
    if 'endTime' in song and 'acousticness' in song:
        month = parse_date(song['endTime']).strftime('%Y-%m')
        monthly_acousticness[month].append(song['acousticness'])

# Calculate average acousticness per month
average_acousticness_per_month = {month: sum(acousticness) / len(acousticness)
                                  for month, acousticness in monthly_acousticness.items()}

# Sort the data by month
sorted_months_acousticness = sorted(average_acousticness_per_month.keys())
sorted_acousticness = [average_acousticness_per_month[month] for month in sorted_months_acousticness]

# Plotting for Acousticness
plt.figure(figsize=(12, 6))
plt.plot(sorted_months_acousticness, sorted_acousticness, marker='o', color='cyan')
plt.xlabel('Month')
plt.ylabel('Average Acousticness')
plt.title('Average Acousticness Per Month')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
