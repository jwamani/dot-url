from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide

from src.application.use_cases import CreateUser
from src.application.dtos.user_dtos import CreateUserRequest
from src.container import Container


router = APIRouter(prefix="/users" ,tags=["Users"])

@router.post("")
async def create_user(request: CreateUserRequest, usecase: CreateUser = Depends(Provide[Container.create_user])):
    return await usecase.execute(request)