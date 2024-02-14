import pytest


def pytest_addoption(parser):
    parser.addoption('--search', action='store', default='pikachu')


@pytest.fixture(scope='function')
def base_url():
    URL = 'https://api.pokemontcg.io/v2/cards'
    return URL


@pytest.fixture(scope='function')
def search(request):
    search_request = request.config.getoption("search")
    return search_request
