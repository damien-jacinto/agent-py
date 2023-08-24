from typing import List
from domain.models import Cpu
from monitor import MonitorTask


class CpuService:
    def __init__(self):
        ...

    async def get_cpu(self, monitorTask: MonitorTask) -> List[Cpu]:
        cpulist = []
        cpulist.append(Cpu(id=1, value=monitorTask.cpu))
        return cpulist
