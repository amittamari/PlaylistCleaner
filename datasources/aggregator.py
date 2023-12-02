#!/usr/bin/env python3

from functools import reduce

from datasources.base import BaseDataSource

class DataSourceAggregator():

    def __init__(self, datasources: list[BaseDataSource] = []) -> None:
        self.datasources = datasources

    def get_playlists(self) -> list:
        all_playlists = [datasource.get_playlists() for datasource in self.datasources]

        return list(filter(None, all_playlists))

    def get_track_playcount(self, track) -> int:
        agg_playcounts = [datasource.get_track_playcount(track) for datasource in self.datasources]

        return reduce(lambda a, b: a+b, list(filter(None, agg_playcounts)))

