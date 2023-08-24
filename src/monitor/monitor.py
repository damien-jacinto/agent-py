import time
import psutil


class MonitorTask:

    cpu: str

    def __init__(self) -> None:
        pass

    def monitor(self):
        while True:
            self.cpu = str(psutil.cpu_times())
            time.sleep(3)
