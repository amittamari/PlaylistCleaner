#!/usr/bin/env python3

from functools import reduce
from typing import Iterable

from datasources.base import BaseDataSource

def filter_none(iterable: Iterable) -> list:
    filtered = filter(None, iterable)
    return list(filtered)

class DataSourceAggregator():

    def __init__(self, datasources: list[BaseDataSource] = []) -> None:
        self.datasources = datasources

    def get_playlists(self) -> list:
        all_playlists = [datasource.get_playlists() for datasource in self.datasources]

        return filter_none(all_playlists)

    def get_track_playcount(self, track) -> int:
        agg_playcounts = [datasource.get_track_playcount(track) for datasource in self.datasources]

        return reduce(
            lambda a, b: a+b,
            filter_none(agg_playcounts)
        )

