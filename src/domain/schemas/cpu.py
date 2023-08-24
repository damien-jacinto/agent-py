from pydantic import BaseModel


class GetCpuResponseSchema(BaseModel):
    id: int
    value: str
