import uuid
from datetime import datetime

from src.cluster.aplication import ClusterCreate, ClusterDelete, ClusterGet, ClusterList
from src.cluster.domain import Cluster, ClusterStates
from src.cluster.infrastructure import RamClusterRepository


def test_cluster_create():
    name = "cluster name"
    repo = RamClusterRepository([])

    result = ClusterCreate(repo).execute(name)

    assert isinstance(result, Cluster)
    assert result.state == ClusterStates.PENDING


def test_list_all_clusters():
    clusters = [
        Cluster(
            id=uuid.uuid4(),
            name="name",
            state=ClusterStates.RUNNING,
            create_on=datetime.now(),
        ),
        Cluster(
            id=uuid.uuid4(),
            name="name",
            state=ClusterStates.RUNNING,
            create_on=datetime.now(),
        ),
        Cluster(
            id=uuid.uuid4(),
            name="name",
            state=ClusterStates.RUNNING,
            create_on=datetime.now(),
        ),
        Cluster(
            id=uuid.uuid4(),
            name="name",
            state=ClusterStates.RUNNING,
            create_on=datetime.now(),
        ),
    ]
    repo = RamClusterRepository(clusters)

    result = ClusterList(repo).execute()

    assert result == clusters


def test_get_cluster_by_id():
    cluster = Cluster(
        id=uuid.uuid4(),
        name="name",
        state=ClusterStates.RUNNING,
        create_on=datetime.now(),
    )
    repo = RamClusterRepository([cluster])

    result = ClusterGet(repo).execute(cluster.id)

    assert cluster == result


def test_delete_cluster():
    cluster = Cluster(
        id=uuid.uuid4(),
        name="name",
        state=ClusterStates.RUNNING,
        create_on=datetime.now(),
    )
    repo = RamClusterRepository([cluster])

    ClusterDelete(repo).execute(cluster.id)

    assert not repo.data
