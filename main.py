#!/usr/bin/env python3

import datasources
from datasources.base import BaseDataSource

import typer

app = typer.Typer(
    name="PlaylistCleaner",
    help="CLI to clean songs you don't listen to anymore from your playlists",
    no_args_is_help=True
)

initialized_datasources: list[BaseDataSource] = []

@app.command(name="Clean")
def clean():
    for datasource in initialized_datasources:
        playlists = datasource.get_playlists()
        print(playlists)

def init():
    # init data sources
    for DatasourceClass in BaseDataSource.__subclasses__():
        try:
            datasource = DatasourceClass()
            initialized_datasources.append(datasource)
        except NotImplementedError as e:
            print(f'Failed to initialize {DatasourceClass.__name__}:', e)

if __name__ == '__main__':
    init()
    app()
