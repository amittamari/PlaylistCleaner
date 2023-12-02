#!/usr/bin/env python3

import typer

app = typer.Typer(
    name="PlaylistCleaner",
    help="CLI to clean songs you don't listen to anymore from your playlists",
    no_args_is_help=True
)

if __name__ == '__main__':
    app()
