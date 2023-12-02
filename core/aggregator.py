#!/usr/bin/env python3

from functools import reduce
from typing import Iterable

from core.base import BaseDataSource, PlaylistDataSource, TrackPlaycountDataSource

def filter_none(iterable: Iterable) -> list:
    filtered = filter(None, iterable)
    return list(filtered)

class DataSourceAggregator():

    def __init__(self, datasources: list[BaseDataSource] = []) -> None:
        self.datasources = datasources

    def __get_playlist_datasources(self) -> list[PlaylistDataSource]:
        return [ds for ds in self.datasources if isinstance(ds, PlaylistDataSource)]

    def __get_track_playcount_datasources(self) -> list[TrackPlaycountDataSource]:
        return [ds for ds in self.datasources if isinstance(ds, TrackPlaycountDataSource)]

    def get_playlists(self) -> list:
        playlist_datasources = self.__get_playlist_datasources()

        return [playlist['name'] for ds in playlist_datasources for playlist in ds.get_playlists()]

    def get_track_playcount(self, track) -> int:
        track_playcount_datasources = self.__get_track_playcount_datasources()
        agg_playcounts = [ds.get_track_playcount(track) for ds in track_playcount_datasources]

        return reduce(
            lambda a, b: a+b,
            agg_playcounts
        )

