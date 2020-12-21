import uuid
from typing import List, Optional

from src.cluster.domain import Cluster, ClusterRepository, ClusterNotFound


class RamClusterRepository(ClusterRepository):
    def __init__(self, data: List[Optional[Cluster]]):
        self.data = data

    def save(self, cluster: Cluster):
        self.data.append(cluster)

    def list(self, filter: Optional[dict] = None) -> List[Cluster]:
        return self.data

    def get(self, id: uuid.UUID) -> Cluster:
        for cluster in self.data:
            if cluster.id == id:
                return cluster
        raise ClusterNotFound(id)

    def delete(self, id: uuid.UUID) -> None:
        pos = None
        for i, cluster in enumerate(self.data):
            if cluster.id == id:
                pos = i
        if pos is not None:
            self.data.pop(pos)
