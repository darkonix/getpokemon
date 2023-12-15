import pytest
import requests
from uuid import UUID, uuid4
from datetime import datetime
import json

base_url = "http://localhost:80/"


def test_root_get():
    res = requests.get(base_url).json()
    pytest.assume("abilities" in res.keys())
    pytest.assume("name" in res.keys())
    pytest.assume(type(res["id"]) == int)


def test_list_get():
    res = requests.get(base_url + "list/?q=15", timeout=30)
    res = json.loads(res.text)[0]
    pytest.assume(res["id"] == 15)
