import uuid
import json
from pathlib import Path
from typing import List, Optional, Dict

from pydantic import BaseModel

from src.cluster.domain import Cluster, ClusterRepository, ClusterNotFound


class RamClusterRepository(ClusterRepository):
    def __init__(self, data: Dict[uuid.UUID, Cluster]):
        self.data = data

    def save(self, cluster: Cluster):
        self.data[cluster.id] = cluster

    def list(self, filter: Optional[dict] = None) -> List[Cluster]:
        return list(self.data.values())

    def get(self, id: uuid.UUID) -> Cluster:
        try:
            return self.data[id]
        except KeyError:
            raise ClusterNotFound(id)

    def delete(self, id: uuid.UUID) -> None:
        try:
            self.data.pop(id)
        except:
            pass


class FileClusterRepository(ClusterRepository):
    def __init__(self, path: str):
        self.path = Path(path)
        if not self.path.is_file():
            self.path.touch()
            with self.path.open("w") as f:
                json.dump({}, f)

    def save(self, cluster: Cluster):
        with self.path.open() as f:
            data = json.load(f)
            data[str(cluster.id)] = cluster.json()
        with self.path.open("w+") as f:
            json.dump(data, f)

    def list(self, filter: Optional[dict] = None) -> List[Cluster]:
        with open(self.path) as f:
            data = json.load(f)
            return [Cluster(**json.loads(i)) for i in data.values()]

    def get(self, id: uuid.UUID) -> Cluster:
        with open(self.path) as f:
            try:
                return json.load(f)[str(id)]
            except KeyError:
                raise ClusterNotFound(id)

    def delete(self, id: uuid.UUID) -> None:
        with self.path.open() as f:
            data = json.load(f)
            try:
                data.pop(str(id))
            except:
                return
        with self.path.open("w+") as f:
            json.dump(data, f)
