import pytest

from converters.decimal import dec_to_bin, dec_to_hex


# =========================
# Decimal → Binary
# =========================

def test_dec_to_bin():
    assert dec_to_bin(0) == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin(2) == "10"
    assert dec_to_bin(10) == "1010"
    assert dec_to_bin(45) == "101101"
    assert dec_to_bin(255) == "11111111"


def test_dec_to_bin_large():
    assert dec_to_bin(1024) == "10000000000"
    assert dec_to_bin(65535) == "1111111111111111"
    assert dec_to_bin(65536) == "10000000000000000"


# =========================
# Decimal → Hex
# =========================

def test_dec_to_hex():
    assert dec_to_hex(0) == "0"
    assert dec_to_hex(1) == "1"
    assert dec_to_hex(10) == "A"
    assert dec_to_hex(15) == "F"
    assert dec_to_hex(16) == "10"
    assert dec_to_hex(45) == "2D"
    assert dec_to_hex(255) == "FF"


def test_dec_to_hex_large():
    assert dec_to_hex(1024) == "400"
    assert dec_to_hex(4096) == "1000"
    assert dec_to_hex(65535) == "FFFF"


# =========================
# Invalid input
# =========================

def test_dec_to_bin_invalid():
    with pytest.raises(ValueError):
        dec_to_bin(-1)


def test_dec_to_hex_invalid():
    with pytest.raises(ValueError):
        dec_to_hex(-1)
