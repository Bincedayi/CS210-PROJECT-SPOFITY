import json
import matplotlib.pyplot as plt
from collections import defaultdict
from dateutil.parser import parse as parse_date

# Load the updated detailed JSON file
with open(r"C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data\PROJEDEN KULLNACAGIM DATA\updated_unique_songs_detayli_formatted.json", encoding='utf-8') as file:
    songs_data = json.load(file)

# Aggregate danceability by month
monthly_danceability = defaultdict(list)
for song in songs_data:
    if 'endTime' in song and 'danceability' in song:
        month = parse_date(song['endTime']).strftime('%Y-%m')
        monthly_danceability[month].append(song['danceability'])

# Calculate average danceability per month
average_danceability_per_month = {month: sum(danceability) / len(danceability)
                                  for month, danceability in monthly_danceability.items()}

# Sort the data by month
sorted_months = sorted(average_danceability_per_month.keys())
sorted_danceability = [average_danceability_per_month[month] for month in sorted_months]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(sorted_months, sorted_danceability, marker='o', color='blue')
plt.xlabel('Month')
plt.ylabel('Average Danceability')
plt.title('Average Danceability Per Month')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
