import uuid

from apps.backend.dependencies import get_cluster_repo
from fastapi import APIRouter, Body, Depends
from src.cluster.aplication import ClusterCreate, ClusterDelete, ClusterGet, ClusterList
from src.cluster.domain import ClusterRepository

router = APIRouter()


@router.post("")
def create(
    name: str = Body(..., embed=True),
    repo: ClusterRepository = Depends(get_cluster_repo),
):
    return ClusterCreate(repo).execute(name)


@router.get("")
def list(repo: ClusterRepository = Depends(get_cluster_repo)):
    return ClusterList(repo).execute()


@router.get("/{id}")
def get(id: uuid.UUID, repo: ClusterRepository = Depends(get_cluster_repo)):
    return ClusterGet(repo).execute(id)


@router.delete("/{id}")
def delete(id: uuid.UUID, repo: ClusterRepository = Depends(get_cluster_repo)):
    ClusterDelete(repo).execute(id)
