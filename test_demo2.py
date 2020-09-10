import pytest

@pytest.mark.xfail
def test_sample2():
    assert 2 + 3 == 4

@pytest.mark.skip
def test_SecondCreditCard():
    msg1 = "Hello Rohith"
    assert msg1 == "Hello Rohith", "Succesfull"

