from converters.binary import bin_to_dec, bin_to_hex
import pytest

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


# =========================
# Binary → Hex
# =========================

def test_bin_to_hex():
    assert bin_to_hex("0") == "0"
    assert bin_to_hex("1") == "1"
    assert bin_to_hex("1010") == "A"
    assert bin_to_hex("1111") == "F"
    assert bin_to_hex("101101") == "2D"
    assert bin_to_hex("11111111") == "FF"



def test_invalid_binary():
    with pytest.raises(ValueError):
        bin_to_dec("10201")

    with pytest.raises(ValueError):
        bin_to_hex("12345")

    with pytest.raises(ValueError):
        bin_to_dec("hello")
