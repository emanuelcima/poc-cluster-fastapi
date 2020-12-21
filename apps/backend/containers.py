from dependency_injector import containers, providers

from src.cluster.infrastructure import RamClusterRepository


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()
    cluster_repo = providers.Singleton(
        RamClusterRepository,
        data={},
    )
