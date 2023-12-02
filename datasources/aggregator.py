#!/usr/bin/env python3

from functools import reduce

from datasources.base import BaseDataSource

class DataSourceAggregator():

    def __init__(self, datasources: list[BaseDataSource] = []) -> None:
        self.datasources = datasources

    def get_playlists(self) -> list:
        all_playlists = []
        for datasource in self.datasources:
            try:
                playlists = datasource.get_playlists()
                all_playlists.append(playlists)
            except NotImplementedError:
                # its ok, the datasource may not implement all methods
                pass

        return all_playlists

    def get_track_playcount(self, track) -> int:
        agg_playcounts = []
        for datasource in self.datasources:
            try:
                playcount = datasource.get_track_playcount(track)
                agg_playcounts.append(playcount)
            except NotImplementedError:
                pass

        return reduce(lambda a, b: a+b, agg_playcounts)

