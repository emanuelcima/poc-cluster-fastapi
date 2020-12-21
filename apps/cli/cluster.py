import uuid

import typer
from dependency_injector.wiring import inject, Provide

from src.cluster.aplication import ClusterCreate, ClusterDelete, ClusterGet, ClusterList
from src.cluster.domain import ClusterRepository
from apps.cli.containers import Container


app = typer.Typer()

@inject
def get_cluster_repo(repo: ClusterRepository = Provide[Container.cluster_repo]):
    return repo


@app.command()
def create(name: str):
    result = ClusterCreate(get_cluster_repo()).execute(name)
    typer.echo(result)


@app.command()
def list():
    result = ClusterList(get_cluster_repo()).execute()
    if not result:
        raise typer.Exit()
    typer.echo(result)


@app.command()
def get(id: uuid.UUID):
    try:
        result = ClusterGet(get_cluster_repo()).execute(id)
    except Exception as error:
        typer.echo(error)
        raise typer.Exit(1)

    typer.echo(result)


@app.command()
def delete(id: uuid.UUID):
    ClusterDelete(get_cluster_repo()).execute(id)
