from src.cluster.domain import ClusterRepository
from src.cluster.infrastructure import RamClusterRepository


class ClusterRepositoryInjector:
    def __init__(self, repo: ClusterRepository):
        self.repo = repo

    def __call__(self):
        return self.repo


ram_cluster_repository = RamClusterRepository([])
get_cluster_repo = ClusterRepositoryInjector(ram_cluster_repository)
