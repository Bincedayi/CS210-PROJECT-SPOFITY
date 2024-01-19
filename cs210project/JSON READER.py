import json
from datetime import datetime
from collections import defaultdict

# Paths to your JSON files
file_paths = [
    r'C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data/StreamingHistory0.json',
    r'C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data/StreamingHistory1.json',
    r'C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data/StreamingHistory2.json',
    r'C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data/StreamingHistory3.json'
]

# Function to load data from a file
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Combine data from all files
streaming_history = []
for file_path in file_paths:
    streaming_history.extend(load_data(file_path))

# Helper function to parse the date from endTime
def parse_date(end_time):
    return datetime.strptime(end_time, '%Y-%m-%d %H:%M').date()

# Process the streaming history
processed_history = defaultdict(set)
excluded_tracks = set()

for entry in streaming_history:
    track_key = (entry['artistName'], entry['trackName'])
    date_played = parse_date(entry['endTime'])

    # Exclude songs played for less than 60 seconds
    if entry['msPlayed'] < 60000:
        excluded_tracks.add(track_key)
        continue

    # Add to processed history, counting each song only once per day
    if track_key not in processed_history[date_played]:
        processed_history[date_played].add(track_key)

# Remove excluded tracks that were played more than once
for date, tracks in processed_history.items():
    processed_history[date] = {track for track in tracks if track not in excluded_tracks}

# Summarize the result
total_days = len(processed_history)
total_unique_tracks = sum(len(tracks) for tracks in processed_history.values())

print(f"Total Days: {total_days}")
print(f"Total Unique Tracks: {total_unique_tracks}")
