import pytest

@pytest.mark.usefixtures("setup")
class TestFixture():


    def test_fixtureDemo1(self):
        print("\nI am the test function1")

    def test_fixtureDemo2(self):
        print("\nI am the test function2")

    def test_fixtureDemo3(self):
        print("\nI am the test function3")
