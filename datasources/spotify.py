#!/usr/bin/env python3

from datasources.base import BaseDataSource

class SpotifyDataSource(BaseDataSource):

    def __init__(self) -> None:
        print('spotify initialized')

    def get_playlists(self) -> list:
        return ["My Playlist 1", "My Playlist 2"]
