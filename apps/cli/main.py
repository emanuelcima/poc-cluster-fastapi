import sys

import typer

from apps.cli.containers import Container
from apps.cli import cluster

container = Container()
container.wire(modules=[cluster])

app = typer.Typer()
app.container = container
app.add_typer(cluster.app, name="cluster")
