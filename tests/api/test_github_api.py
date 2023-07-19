import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists():
    api = GitHub()
    user = api.get_user_defunkt()
    assert user["login"] == "defunkt"


# First print(r) to see what we can use in the assert
@pytest.mark.api
def test_user_not_exists_print():
    api = GitHub()
    r = api.get_non_exist_user()
    print(r)


@pytest.mark.api
def test_user_not_exists():
    api = GitHub()
    r = api.get_non_exist_user()
    assert r["message"] == "Not Found"
