import abc
import uuid
from datetime import datetime
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel


class ClusterStates(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"


class Cluster(BaseModel):
    id: uuid.UUID
    name: str
    state: ClusterStates
    create_on: datetime


class ClusterRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, cluster: Cluster) -> None:
        pass

    @abc.abstractmethod
    def list(self, filter: Optional[dict] = None) -> List[Cluster]:
        pass

    @abc.abstractmethod
    def get(self, id: uuid.UUID) -> Cluster:
        pass

    @abc.abstractmethod
    def delete(self, id: uuid.UUID) -> None:
        pass


class ClusterNotFound(Exception):
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"ClusterNotFound, id: {self.id}"

    def __str__(self):
        return self.__repr__()
