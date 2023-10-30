import threading
from fastapi.testclient import TestClient
from server import app
from monitor import MonitorTask


class MonitorTaskFake(MonitorTask):

    interval: int = 0
    cpu_percent: list[float] = ["10", "12"]
    num_cores: int = 3

    def monitor(self):
        pass


client = TestClient(app)
thread = threading.Thread(target=app.state.monitortask.monitor, daemon=True)
thread.start()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_get_cpu_usage():
    save_app = app.state.monitortask
    app.state.monitortask = MonitorTaskFake()
    response = client.get("/metrics/v1/cpu/usage")
    assert response.status_code == 200
    assert response.json() == [{"id": 0, "usage": "10"}, {"id": 1, "usage": "12"}]
    app.state.monitortask = save_app


def test_get_cpu_core():
    response = client.get("/metrics/v1/cpu/core")
    assert response.status_code == 200
    assert isinstance(response.json()["number"], int)
