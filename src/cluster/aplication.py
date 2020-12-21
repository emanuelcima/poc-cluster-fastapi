import uuid
from datetime import datetime
from typing import List

from src.cluster.domain import Cluster, ClusterRepository, ClusterStates


class ClusterCreate:
    def __init__(self, repo: ClusterRepository):
        self.repo = repo

    def execute(self, name: str) -> Cluster:
        new_cluster = Cluster(
            id=uuid.uuid4(),
            name=name,
            state=ClusterStates.PENDING,
            create_on=datetime.now(),
        )

        self.repo.save(new_cluster)

        return new_cluster


class ClusterList:
    def __init__(self, repo: ClusterRepository):
        self.repo = repo

    def execute(self) -> List[Cluster]:
        return self.repo.list()


class ClusterGet:
    def __init__(self, repo: ClusterRepository):
        self.repo = repo

    def execute(self, id: uuid.UUID) -> Cluster:
        return self.repo.get(id)


class ClusterDelete:
    def __init__(self, repo: ClusterRepository):
        self.repo = repo

    def execute(self, id: uuid.UUID) -> None:
        self.repo.delete(id)
