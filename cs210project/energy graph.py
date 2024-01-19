import json
import matplotlib.pyplot as plt
from collections import defaultdict
from dateutil.parser import parse as parse_date

# Load the updated detailed JSON file
with open(r"C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data\PROJEDEN KULLNACAGIM DATA\updated_unique_songs_detayli_formatted.json", encoding='utf-8') as file:
    songs_data = json.load(file)

# Aggregate energy by month
monthly_energy = defaultdict(list)
for song in songs_data:
    if 'endTime' in song and 'energy' in song:
        month = parse_date(song['endTime']).strftime('%Y-%m')
        monthly_energy[month].append(song['energy'])

# Calculate average energy per month
average_energy_per_month = {month: sum(energy) / len(energy)
                            for month, energy in monthly_energy.items()}

# Sort the data by month
sorted_months_energy = sorted(average_energy_per_month.keys())
sorted_energy = [average_energy_per_month[month] for month in sorted_months_energy]

# Plotting for Energy
plt.figure(figsize=(12, 6))
plt.plot(sorted_months_energy, sorted_energy, marker='o', color='green')
plt.xlabel('Month')
plt.ylabel('Average Energy')
plt.title('Average Energy Per Month')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
