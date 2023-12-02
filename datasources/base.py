#!/usr/bin/env python3

from abc import ABC, abstractmethod

class BaseDataSource(ABC):

    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError('__init__ not implemented')

    def get_playlists(self) -> list:
        raise NotImplementedError('get_playlists not implemented')

    def get_track_playcount(self) -> int:
        raise NotImplementedError('get_track_playcount not implemented')
