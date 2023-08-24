from pydantic import BaseModel


class Cpu(BaseModel):
    id: int
    value: str
