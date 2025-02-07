pytest_plugins = (
    "tests.fixtures.client",
    "tests.fixtures.fake",
    "tests.fixtures.channels",
    "tests.fixtures.users",
)


def pytest_make_parametrize_id(config, val):
    return repr(val)
