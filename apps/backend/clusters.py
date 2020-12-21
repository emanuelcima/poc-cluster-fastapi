import uuid

from fastapi import APIRouter, Body, Depends, status, HTTPException
from dependency_injector.wiring import inject, Provide

from src.cluster.aplication import ClusterCreate, ClusterDelete, ClusterGet, ClusterList
from src.cluster.domain import ClusterRepository
from apps.backend.containers import Container

router = APIRouter()


@router.post("")
@inject
def create(
    name: str = Body(..., embed=True),
    repo: ClusterRepository = Depends(Provide[Container.cluster_repo]),
):
    return ClusterCreate(repo).execute(name)


@router.get("")
@inject
def list(repo: ClusterRepository = Depends(Provide[Container.cluster_repo])):
    return ClusterList(repo).execute()


@router.get("/{id}")
@inject
def get(
    id: uuid.UUID, repo: ClusterRepository = Depends(Provide[Container.cluster_repo])
):
    try:
        return ClusterGet(repo).execute(id)
    except Exception as error:
        raise HTTPException(status.HTTP_404_NOT_FOUND, str(error))


@router.delete("/{id}")
@inject
def delete(
    id: uuid.UUID, repo: ClusterRepository = Depends(Provide[Container.cluster_repo])
):
    ClusterDelete(repo).execute(id)
