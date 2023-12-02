#!/usr/bin/env python3

import json

from datasources.base import BaseDataSource

SPOTIFY_SCOPES = 'playlist-read-private'
SECRETS_SPOTIFY_CLIENT_ID = 'spotify-api-clientid'
SECRETS_SPOTIFY_SECRET = 'spotify-api-secret'
SECRETS_SPOTIFY_REDIRECT_URI = 'spotify-api-redirect-uri'

class SpotifyDataSource(BaseDataSource):

    def __init__(self) -> None:
        print("init SpotifyDataSource")
        SpotifyDataSource.connect_to_spotify()

    def get_playlists(self) -> list:
        return ["My Playlist 1", "My Playlist 2"]

    @staticmethod
    def connect_to_spotify(
        secrets_path="secrets.json"
    ):
        pass
        # f = open(file="secrets.json")
        # secrets = json.load(f)
        # print(secrets)
