from pydantic import BaseModel
from .cpu import GetCpuResponseSchema


class ExceptionResponseSchema(BaseModel):
    error: str


__all__ = [
    "GetCpuResponseSchema",
    "ExceptionResponseSchema",
]
