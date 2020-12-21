from dependency_injector import containers, providers

from src.cluster.infrastructure import FileClusterRepository


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()
    cluster_repo = providers.Singleton(
        FileClusterRepository,
        path=".file-cluster-repo",
    )
