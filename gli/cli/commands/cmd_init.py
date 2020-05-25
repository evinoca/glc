from __future__ import absolute_import
from __future__ import unicode_literals

import click

from gli.cli.entry import pass_environment


@click.command("init", short_help="Initializes a repo.")
@click.argument("path", required=False, type=click.Path(resolve_path=True))
@pass_environment
def cli(ctx, path):
    """Initializes a repository."""
    if path is None:
        path = ctx.home
    ctx.log(f"Initialized the repository in {click.format_filename(path)}")
