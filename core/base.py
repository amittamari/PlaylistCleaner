#!/usr/bin/env python3

from abc import ABC, abstractmethod

class BaseDataSource(ABC):

    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError('__init__ not implemented')

class PlaylistDataSource(BaseDataSource):

    @abstractmethod
    def get_playlists(self) -> list:
        pass

class TrackPlaycountDataSource(BaseDataSource):

    @abstractmethod
    def get_track_playcount(self, track) -> int:
        pass
