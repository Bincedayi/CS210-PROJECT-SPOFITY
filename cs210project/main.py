import requests
import base64
import json
import time

# Spotify API credentials
client_id = '6eb5afb831d345c585b27f05b5fbdbae'
client_secret = '4c9e22db297941c5a752aed7310f4881'

# Function to obtain access token
def get_access_token(client_id, client_secret):
    # Encode as Base64
    client_creds = f"{client_id}:{client_secret}"
    client_creds_b64 = base64.b64encode(client_creds.encode())

    # Spotify Token URL
    token_url = "https://accounts.spotify.com/api/token"
    token_data = {
        "grant_type": "client_credentials"
    }
    token_headers = {
        "Authorization": f"Basic {client_creds_b64.decode()}"
    }

    # Make a POST request
    r = requests.post(token_url, data=token_data, headers=token_headers)
    token_response_data = r.json()
    access_token = token_response_data['access_token']

    return access_token

def make_request_with_rate_limit_handling(url, headers):
    while True:
        response = requests.get(url, headers=headers)
        if response.status_code == 429:  # Rate limit exceeded
            retry_after = int(response.headers.get('Retry-After', 1))  # Default to 1 second if header is missing
            print(f"Rate limit exceeded, retrying after {retry_after} seconds.")
            time.sleep(retry_after)
        else:
            return response

def get_track_id(track_name, artist_name, access_token):
    query = f"track:{track_name} artist:{artist_name}"
    search_url = f"https://api.spotify.com/v1/search?q={query}&type=track"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = make_request_with_rate_limit_handling(search_url, headers)

    print(f"Searching for '{track_name}' by '{artist_name}'")

    # Check for non-200 status codes
    if response.status_code != 200:
        print(f"Error fetching track ID for {track_name} by {artist_name}: {response.status_code} - {response.text}")
        return None

    search_results = response.json()

    if 'tracks' in search_results and search_results['tracks']['items']:
        track_id = search_results['tracks']['items'][0]['id']
        print(f"Found track ID for '{track_name}': {track_id}")  # Print the found track ID
        return track_id
    else:
        print(f"No track ID found for '{track_name}'")  # Print if no track ID is found
        return None

def get_audio_features(track_id, access_token):
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = make_request_with_rate_limit_handling(url, headers)

    audio_features = response.json()
    print(f"Audio features for track ID {track_id}: {audio_features}")  # Print the audio features
    return audio_features

    # Check for non-200 status codes
    if response.status_code != 200:
        print(f"Error fetching audio features for track ID {track_id}: {response.status_code} - {response.text}")
        return None

    return response.json()


# Main
access_token = get_access_token(client_id, client_secret)

# Load the unique songs from the file
with open(r'C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data/corrected_final_tracks_with_endtime.json', encoding='utf-8') as file:
    unique_songs = json.load(file)

# Prepare a list to store the results
song_features = []

for song in unique_songs:
    track_id = get_track_id(song['trackName'], song['artistName'], access_token)
    print(f"Processing {song['trackName']} by {song['artistName']}")  # Logging progress
    if track_id:
        features = get_audio_features(track_id, access_token)
        if features is not None:
            # Extract only the desired features
            desired_features = {key: features[key] for key in ['danceability', 'energy', 'key', 'loudness', 'mode',
                                                              'speechiness', 'acousticness', 'instrumentalness',
                                                              'liveness', 'valence', 'tempo']}
            song_features.append({'artistName': song['artistName'], 'trackName': song['trackName'], **desired_features})
        else:
            print(f"Skipping song {song['trackName']} by {song['artistName']} due to error fetching features.")

# Save the results to a file
output_file_path = r'C:\Users\PC\Desktop\CS210 PROJE SPOTIFY\kullanacagin dosya bu\my_spotify_data\Spotify Account Data/unique songs detayli.json'
with open(output_file_path, 'w') as outfile:
    json.dump(song_features, outfile, indent=4)

# Note: Replace 'path_to_your_file/UniqueSongs.json' and 'path_to_your_output_file/song_features.json'
# with the actual paths to your input and output files.
# Also, replace 'your_client_id' and 'your_client_secr-et' with your Spotify API credentials.