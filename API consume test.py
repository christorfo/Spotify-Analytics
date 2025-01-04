import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def initialize_spotify_api(client_id, client_secret):
    """
    Initialize the Spotify API client with the provided credentials.

    Args:
        client_id (str): Spotify API client ID.
        client_secret (str): Spotify API client secret.

    Returns:
        spotipy.Spotify: Authenticated Spotify API client.
    """
    credentials_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    )
    return spotipy.Spotify(client_credentials_manager=credentials_manager)

def search_tracks(sp, query, limit=10):
    """
    Search for tracks on Spotify based on a query string.

    Args:
        sp (spotipy.Spotify): Authenticated Spotify API client.
        query (str): Search query (e.g., song title or artist).
        limit (int): Number of results to return (default is 10).

    Returns:
        list: List of dictionaries containing track details.
    """
    results = sp.search(q=query, type='track', limit=limit)
    tracks = results.get('tracks', {}).get('items', [])

    return [
        {
            "name": track.get('name'),
            "artist": track.get('artists')[0].get('name') if track.get('artists') else 'Unknown Artist',
            "url": track.get('external_urls', {}).get('spotify', 'No URL')
        }
        for track in tracks
    ]

def display_tracks(tracks):
    """
    Display a list of tracks in a formatted way.

    Args:
        tracks (list): List of dictionaries containing track details.
    """
