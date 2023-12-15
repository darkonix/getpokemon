import pytest
from uuid import uuid4
from time import sleep
from datetime import datetime
from main import root, get_list
import json
import asyncio
from fastapi import Query


def test_root_get():
    res = asyncio.run(root())
    pytest.assume("abilities" in res.keys())
    pytest.assume("name" in res.keys())
    pytest.assume(type(res["id"]) == int)


def test_list_get():
    res = asyncio.run(get_list(q=[15]))[0]
    pytest.assume(res["id"] == 15)
