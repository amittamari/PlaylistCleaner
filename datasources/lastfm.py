#!/usr/bin/env python3

from core.types import TrackPlaycountDataSource

class LastFmDataSource(TrackPlaycountDataSource):

    def __init__(self) -> None:
        print('init LastFmDataSource')

    def get_track_playcount(self ,_) -> int:
        return 3
