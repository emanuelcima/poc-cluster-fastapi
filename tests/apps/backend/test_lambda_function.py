import uuid
import json
from datetime import datetime

from fastapi.testclient import TestClient
import pytest

from apps.backend.lambda_function import app
from src.cluster.domain import Cluster, ClusterStates, ClusterNotFound
from src.cluster.infrastructure import RamClusterRepository


test_client = TestClient(app)


def test_cluster_create():
    ram_cluster_repo = RamClusterRepository({})
    with app.container.cluster_repo.override(ram_cluster_repo):
        response = test_client.post("/clusters", json={"name": "cluster_name"})
        ram_cluster_repo.get(uuid.UUID(response.json()["id"]))


def test_cluster_list():
    data = {}
    for i in range(4):
        id = uuid.uuid4()
        data[id] = Cluster(
            id=id,
            name=f"name-{i}",
            state=ClusterStates.RUNNING,
            create_on=datetime.now(),
        )
    ram_cluster_repo = RamClusterRepository(data)

    with app.container.cluster_repo.override(ram_cluster_repo):
        response = test_client.get("/clusters")

    assert len(response.json()) == 4


def test_cluster_get():
    cluster = Cluster(
        id=uuid.uuid4(),
        name="name",
        state=ClusterStates.RUNNING,
        create_on=datetime.now(),
    )
    ram_cluster_repo = RamClusterRepository({cluster.id: cluster})

    with app.container.cluster_repo.override(ram_cluster_repo):
        response = test_client.get("/clusters/" + str(cluster.id))

    assert Cluster(**response.json()) == cluster


def test_cluster_delete():
    cluster = Cluster(
        id=uuid.uuid4(),
        name="name",
        state=ClusterStates.RUNNING,
        create_on=datetime.now(),
    )
    ram_cluster_repo = RamClusterRepository({cluster.id: cluster})

    with app.container.cluster_repo.override(ram_cluster_repo):
        response = test_client.delete("/clusters/" + str(cluster.id))

    with pytest.raises(ClusterNotFound):
        ram_cluster_repo.get(cluster.id)
