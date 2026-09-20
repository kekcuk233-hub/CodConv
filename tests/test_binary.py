import pytest

from converters.binary import bin_to_dec, bin_to_hex


# =========================
# Binary → Decimal
# =========================

def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec("1") == 1
    assert bin_to_dec("10") == 2
    assert bin_to_dec("1010") == 10
    assert bin_to_dec("101101") == 45
    assert bin_to_dec("11111111") == 255


def test_bin_to_dec_large():
    assert bin_to_dec("10000000000") == 1024
    assert bin_to_dec("1111111111111111") == 65535
    assert bin_to_dec("10000000000000000") == 65536


def test_bin_to_dec_invalid():
    with pytest.raises(ValueError):
        bin_to_dec("2")

    with pytest.raises(ValueError):
        bin_to_dec("10201")

    with pytest.raises(ValueError):
        bin_to_dec("abc")

    with pytest.raises(ValueError):
        bin_to_dec("10a01")


def test_bin_to_dec_empty():
    with pytest.raises(ValueError):
        bin_to_dec("")


# =========================
# Binary → Hex
# =========================

def test_bin_to_hex():
    assert bin_to_hex("0") == "0"
    assert bin_to_hex("1") == "1"
    assert bin_to_hex("10") == "2"
    assert bin_to_hex("1010") == "A"
    assert bin_to_hex("1111") == "F"
    assert bin_to_hex("101101") == "2D"
    assert bin_to_hex("11111111") == "FF"


def test_bin_to_hex_large():
    assert bin_to_hex("10000000000") == "400"
    assert bin_to_hex("1111111111111111") == "FFFF"
    assert bin_to_hex("1111111100000000") == "FF00"


def test_bin_to_hex_invalid():
    with pytest.raises(ValueError):
        bin_to_hex("2")

    with pytest.raises(ValueError):
        bin_to_hex("10201")

    with pytest.raises(ValueError):
        bin_to_hex("abc")

    with pytest.raises(ValueError):
        bin_to_hex("10a01")


def test_bin_to_hex_empty():
    with pytest.raises(ValueError):
        bin_to_hex("")
