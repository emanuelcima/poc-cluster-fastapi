import uuid
from datetime import datetime

from src.cluster.domain import Cluster, ClusterStates


def test_cluster_model_init():
    id = uuid.uuid4()
    name = "cluster name"
    state = ClusterStates.RUNNING
    create_on = datetime.now()

    cluster = Cluster(id=id, name=name, state=state, create_on=create_on)

    assert cluster.id == id
    assert cluster.name == name
    assert cluster.state == state
    assert cluster.create_on == create_on
