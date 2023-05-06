import requests
import random

# Replace YOUR_ACCESS_TOKEN with your actual access token
headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}

# Generate a random number between 0 and 999999999 to use as the track ID
track_id = str(random.randint(0, 999999999))

# Make a GET request to the Spotify Web API to retrieve the track information
response = requests.get(f"https://api.spotify.com/v1/tracks/{track_id}", headers=headers)

# If the response is successful, return the name of the track
if response.status_code == 200:
    track_info = response.json()
    track_name = track_info["name"]
    print(track_name)
else:
    print("Error retrieving track information")
