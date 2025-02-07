import os

import pytest

from aiommost.client import MattermostClient


@pytest.fixture
def client():
    host = os.environ["TEST_MM_HOST"]
    token = os.environ["TEST_MM_TOKEN"]

    return MattermostClient(host, token)


@pytest.fixture
def simple_bot_client():
    host = os.environ["TEST_MM_HOST"]
    token = os.environ["TEST_MM_SIMPLE_TOKEN"]

    return MattermostClient(host, token)
