import json
import matplotlib.pyplot as plt
from collections import defaultdict
from dateutil.parser import parse as parse_date

# Load the updated detailed JSON file
with open(r"C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data\PROJEDEN KULLNACAGIM DATA\updated_unique_songs_detayli_formatted.json", encoding='utf-8') as file:
    songs_data = json.load(file)

# Aggregate speechiness by month
monthly_speechiness = defaultdict(list)
for song in songs_data:
    if 'endTime' in song and 'speechiness' in song:
        month = parse_date(song['endTime']).strftime('%Y-%m')
        monthly_speechiness[month].append(song['speechiness'])

# Calculate average speechiness per month
average_speechiness_per_month = {month: sum(speechiness) / len(speechiness)
                                 for month, speechiness in monthly_speechiness.items()}

# Sort the data by month
sorted_months_speechiness = sorted(average_speechiness_per_month.keys())
sorted_speechiness = [average_speechiness_per_month[month] for month in sorted_months_speechiness]

# Plotting for Speechiness
plt.figure(figsize=(12, 6))
plt.plot(sorted_months_speechiness, sorted_speechiness, marker='o', color='orange')
plt.xlabel('Month')
plt.ylabel('Average Speechiness')
plt.title('Average Speechiness Per Month')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
