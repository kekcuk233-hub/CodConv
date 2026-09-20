import pytest

from converters.hex import hex_to_bin, hex_to_dec


# =========================
# Hex → Binary
# =========================

def test_hex_to_bin():
    assert hex_to_bin("0") == "0"
    assert hex_to_bin("1") == "1"
    assert hex_to_bin("2") == "10"
    assert hex_to_bin("A") == "1010"
    assert hex_to_bin("F") == "1111"
    assert hex_to_bin("2D") == "101101"
    assert hex_to_bin("FF") == "11111111"


def test_hex_to_bin_lowercase():
    assert hex_to_bin("a") == "1010"
    assert hex_to_bin("f") == "1111"
    assert hex_to_bin("2d") == "101101"
    assert hex_to_bin("ff") == "11111111"


def test_hex_to_bin_large():
    assert hex_to_bin("400") == "10000000000"
    assert hex_to_bin("FFFF") == "1111111111111111"
    assert hex_to_bin("FF00") == "1111111100000000"


# =========================
# Hex → Decimal
# =========================

def test_hex_to_dec():
    assert hex_to_dec("0") == 0
    assert hex_to_dec("1") == 1
    assert hex_to_dec("A") == 10
    assert hex_to_dec("F") == 15
    assert hex_to_dec("10") == 16
    assert hex_to_dec("2D") == 45
    assert hex_to_dec("FF") == 255


def test_hex_to_dec_lowercase():
    assert hex_to_dec("a") == 10
    assert hex_to_dec("f") == 15
    assert hex_to_dec("2d") == 45
    assert hex_to_dec("ff") == 255


def test_hex_to_dec_large():
    assert hex_to_dec("400") == 1024
    assert hex_to_dec("FFFF") == 65535
    assert hex_to_dec("10000") == 65536


# =========================
# Invalid input
# =========================

def test_hex_to_bin_invalid():
    with pytest.raises(ValueError):
        hex_to_bin("G")

    with pytest.raises(ValueError):
        hex_to_bin("XYZ")

    with pytest.raises(ValueError):
        hex_to_bin("1G")

    with pytest.raises(ValueError):
        hex_to_bin("")


def test_hex_to_dec_invalid():
    with pytest.raises(ValueError):
        hex_to_dec("G")

    with pytest.raises(ValueError):
        hex_to_dec("XYZ")

    with pytest.raises(ValueError):
        hex_to_dec("1G")

    with pytest.raises(ValueError):
        hex_to_dec("")

def test_hex_to_bin_leading_zeros():
    assert hex_to_bin("0A") == "1010"
    assert hex_to_bin("00FF") == "11111111"
    assert hex_to_bin("0002D") == "101101"

def test_hex_to_bin_zero():
    assert hex_to_bin("0") == "0"
    assert hex_to_bin("00") == "0"
    assert hex_to_bin("0000") == "0"
