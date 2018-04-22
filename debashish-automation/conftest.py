

def pytest_addoption(parser):
    parser.addoption("--type", default="Firefox")
    parser.addoption("--env", default="local")
