import pytest

from app import app
from calculator import calculate


@pytest.fixture
def client():
    return app.test_client()


def test_add():
    assert calculate(2, 3, "+") == 5


def test_subtract():
    assert calculate(5, 3, "-") == 2


def test_multiply():
    assert calculate(4, 3, "*") == 12


def test_divide():
    assert calculate(10, 4, "/") == 2.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(1, 0, "/")


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"


def test_api_calculate(client):
    res = client.post("/api/calculate", json={"a": 6, "b": 3, "op": "*"})
    assert res.status_code == 200
    assert res.get_json()["result"] == 18


def test_api_divide_by_zero(client):
    res = client.post("/api/calculate", json={"a": 1, "b": 0, "op": "/"})
    assert res.status_code == 400
