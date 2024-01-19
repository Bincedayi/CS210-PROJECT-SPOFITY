import json
import matplotlib.pyplot as plt
from collections import defaultdict
from dateutil.parser import parse as parse_date

# Load the updated detailed JSON file
with open(r"C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data\PROJEDEN KULLNACAGIM DATA\updated_unique_songs_detayli_formatted.json", encoding='utf-8') as file:
    songs_data = json.load(file)

# Aggregate key by month
monthly_keys = defaultdict(list)
for song in songs_data:
    if 'endTime' in song and 'key' in song:
        month = parse_date(song['endTime']).strftime('%Y-%m')
        monthly_keys[month].append(song['key'])

# Calculate average key per month
average_key_per_month = {month: sum(keys) / len(keys)
                         for month, keys in monthly_keys.items()}

# Sort the data by month
sorted_months_key = sorted(average_key_per_month.keys())
sorted_keys = [average_key_per_month[month] for month in sorted_months_key]

# Plotting for Key
plt.figure(figsize=(12, 6))
plt.plot(sorted_months_key, sorted_keys, marker='o', color='purple')
plt.xlabel('Month')
plt.ylabel('Average Musical Key')
plt.title('Average Musical Key Per Month')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
