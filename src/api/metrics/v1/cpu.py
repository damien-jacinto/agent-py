from typing import List

from fastapi import APIRouter, Request

from domain.schemas import (
    ExceptionResponseSchema,
    GetCpuResponseSchema,
)
from domain.services import CpuService

cpu_router = APIRouter()


@cpu_router.get(
    "",
    response_model=List[GetCpuResponseSchema],
    response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def get_cpu(request: Request) -> List[GetCpuResponseSchema]:
    return await CpuService().get_cpu(request.app.state.monitortask)
