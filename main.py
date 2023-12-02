#!/usr/bin/env python3

from core.aggregator import DataSourceAggregator
from core.initialize import initialize_datasources

import typer

app = typer.Typer(
    name="PlaylistCleaner",
    help="CLI to clean songs you don't listen to anymore from your playlists",
    no_args_is_help=True
)

aggregator: type[DataSourceAggregator] = None

@app.command(name="Clean")
def clean():
    print('')
    print('## CLEAN ##')

    all_playlists = aggregator.get_playlists()
    print(all_playlists)

    playcount = aggregator.get_track_playcount('Meni Mamtera')
    print(playcount)

def init():
        try:
            datasources = initialize_datasources()
            global aggregator
            aggregator = DataSourceAggregator(datasources)
        except NotImplementedError as e:
            print('Failed to initialize', e)

if __name__ == '__main__':
    init()
    app()
