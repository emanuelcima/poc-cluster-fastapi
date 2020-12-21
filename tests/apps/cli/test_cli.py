from typer.testing import CliRunner

from apps.cli.main import app
from src.cluster.infrastructure import RamClusterRepository

runner = CliRunner()


def test_cluster_create():
    ram_cluster_repo = RamClusterRepository({})
    with app.container.cluster_repo.override(ram_cluster_repo):
        result = runner.invoke(app, ["cluster", "create", "name"])
    assert ram_cluster_repo.list()[0].name == "name"

def test_cluster_list():
    pass


def test_list_zero_clusters():
    ram_cluster_repo = RamClusterRepository({})
    with app.container.cluster_repo.override(ram_cluster_repo):
        result = runner.invoke(app, ["cluster", "list"])
    assert result.exit_code == 0
    assert result.output == ""


def test_cluster_get():
    pass


def test_cluster_get_does_not_exist():
    pass


def test_cluster_delete():
    pass
