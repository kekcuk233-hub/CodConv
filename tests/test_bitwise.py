import pytest
from converters.binary import AND, OR


def test_and():
    assert AND("0", "0") == "0"
    assert AND("0", "1") == "0"
    assert AND("1", "0") == "0"
    assert AND("1", "1") == "1"

    assert AND("1010", "1100") == "1000"
    assert AND("1111", "1010") == "1010"
    assert AND("101101", "111111") == "101101"

    assert AND("1010", "10") == "10"
    assert AND("10", "1010") == "10"

    assert AND("1111", "0000") == "0"


def test_or():
    assert OR("0", "0") == "0"
    assert OR("0", "1") == "1"
    assert OR("1", "0") == "1"
    assert OR("1", "1") == "1"

    assert OR("1010", "1100") == "1110"
    assert OR("1111", "1010") == "1111"
    assert OR("101101", "111111") == "111111"

    assert OR("1010", "10") == "1010"
    assert OR("10", "1010") == "1010"

    assert OR("0000", "0000") == "0"

def test_and_invalid():
    with pytest.raises(ValueError):
        AND("10102", "1100")

    with pytest.raises(ValueError):
        AND("", "1100")


def test_or_invalid():
    with pytest.raises(ValueError):
        OR("10102", "1100")

    with pytest.raises(ValueError):
        OR("", "1100")
