import pytest

@pytest.fixture(scope="class")
def setup():
    print("\nI am going to execute first")
    yield
    print("\n I am going to execute last")

@pytest.fixture()
def importData():
    return ("Rohith",1,"GKrishna")


@pytest.fixture(params=[("Name","Rohith"),("Age",27)])
def paramData(request):
    return request.param