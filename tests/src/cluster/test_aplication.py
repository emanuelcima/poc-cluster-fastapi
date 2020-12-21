import uuid
from datetime import datetime

from src.cluster.aplication import ClusterCreate, ClusterDelete, ClusterGet, ClusterList
from src.cluster.domain import Cluster, ClusterStates
from src.cluster.infrastructure import RamClusterRepository


def test_cluster_create():
    name = "cluster name"
    repo = RamClusterRepository({})

    result = ClusterCreate(repo).execute(name)

    assert isinstance(result, Cluster)
    assert result.state == ClusterStates.PENDING


def test_list_all_clusters():
    data = {}
    for i in range(4):
        id = uuid.uuid4()
        data[id] = Cluster(
            id=id,
            name=f"name-{i}",
            state=ClusterStates.RUNNING,
            create_on=datetime.now(),
        )
    repo = RamClusterRepository(data)

    result = ClusterList(repo).execute()

    assert result == list(data.values())


def test_get_cluster_by_id():
    cluster = Cluster(
        id=uuid.uuid4(),
        name="name",
        state=ClusterStates.RUNNING,
        create_on=datetime.now(),
    )
    repo = RamClusterRepository({cluster.id: cluster})

    result = ClusterGet(repo).execute(cluster.id)

    assert cluster == result


def test_delete_cluster():
    cluster = Cluster(
        id=uuid.uuid4(),
        name="name",
        state=ClusterStates.RUNNING,
        create_on=datetime.now(),
    )
    repo = RamClusterRepository({cluster.id: cluster})

    ClusterDelete(repo).execute(cluster.id)

    assert not repo.data
