import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace these with your Spotify API credentials
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"

def search_spotify_tracks(query, limit=10):
    """
    Search for tracks on Spotify based on a query string.
    """
    # Set up authentication with Spotify API
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    # Search for tracks
    results = sp.search(q=query, type='track', limit=limit)
    tracks = results.get('tracks', {}).get('items', [])
    
    # Print track details
    for idx, track in enumerate(tracks):
        name = track.get('name')
        artist = track.get('artists')[0].g
