#!/usr/bin/env python3

import json

from core.types import PlaylistDataSource
from utils import secrets_path

import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_SCOPES = 'playlist-read-private'
SECRETS_SPOTIFY_CLIENT_ID = 'spotify-api-clientid'
SECRETS_SPOTIFY_SECRET = 'spotify-api-secret'
SECRETS_SPOTIFY_REDIRECT_URI = 'spotify-api-redirect_uri'
CACHE_PATH = 'cache_file'

class SpotifyDataSource(PlaylistDataSource):

    def __init__(self) -> None:
        print("init SpotifyDataSource")
        self.spotify = SpotifyDataSource.connect_to_spotify()

    def get_playlists(self) -> list:
        return self.spotify.current_user_playlists(limit=5)['items']

    @staticmethod
    def connect_to_spotify():
        f = open(secrets_path())
        secrets = json.load(f)
        spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
            scope=SPOTIFY_SCOPES,
            client_id=secrets[SECRETS_SPOTIFY_CLIENT_ID],
            client_secret=secrets[SECRETS_SPOTIFY_SECRET],
            redirect_uri=secrets[SECRETS_SPOTIFY_REDIRECT_URI],
            cache_path=CACHE_PATH
        ))

        return spotify
