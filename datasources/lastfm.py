#!/usr/bin/env python3

from datasources.base import BaseDataSource

class LastFmDataSource(BaseDataSource):
    def __init__(self) -> None:
        print('init LastFmDataSource')

    def get_track_playcount(self ,_) -> int:
        return 3
