import random

import pytest

pytest_plugins = (
    "tests.fixtures.client",
    "tests.fixtures.fake",
    "tests.fixtures.channels",
    "tests.fixtures.teams",
    "tests.fixtures.users",
)


def pytest_make_parametrize_id(config, val):
    return repr(val)


@pytest.fixture
def not_existing_id(faker):
    return faker.uuid4()


@pytest.fixture(scope="session", autouse=True)
def faker_seed():
    return random.random()  # noqa: S311
