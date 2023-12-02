#!/usr/bin/env python3

from datasources.aggregator import DatasourceAggregator
from datasources.base import BaseDataSource

import typer

app = typer.Typer(
    name="PlaylistCleaner",
    help="CLI to clean songs you don't listen to anymore from your playlists",
    no_args_is_help=True
)

aggregator: type[DatasourceAggregator] = None

@app.command(name="Clean")
def clean():
    print('')
    print('## CLEAN ##')

    all_playlists = aggregator.get_playlists()
    print(all_playlists)

    playcount = aggregator.get_track_playcount('Meni Mamtera')
    print(playcount)

def init():
    # init data sources
    initialized_datasources: list[BaseDataSource] = []
    for DatasourceClass in BaseDataSource.__subclasses__():
        try:
            datasource = DatasourceClass()
            initialized_datasources.append(datasource)
        except NotImplementedError as e:
            print(f'Failed to initialize {DatasourceClass.__name__}:', e)

        global aggregator
        aggregator = DatasourceAggregator(initialized_datasources)

if __name__ == '__main__':
    init()
    app()
