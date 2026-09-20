from converters.binary import bin_to_dec, bin_to_hex
from converters.decimal import dec_to_bin, dec_to_hex
from converters.hex import hex_to_bin, hex_to_dec


# =========================
# Decimal ↔ Binary
# =========================

def test_decimal_binary_roundtrip():
    values = [
        0,
        1,
        2,
        10,
        15,
        16,
        42,
        45,
        100,
        255,
        1024,
        65535,
    ]

    for value in values:
        assert bin_to_dec(dec_to_bin(value)) == value


# =========================
# Decimal ↔ Hex
# =========================

def test_decimal_hex_roundtrip():
    values = [
        0,
        1,
        2,
        10,
        15,
        16,
        42,
        45,
        100,
        255,
        1024,
        65535,
    ]

    for value in values:
        assert hex_to_dec(dec_to_hex(value)) == value


# =========================
# Binary → Hex → Binary
# =========================

def test_binary_hex_roundtrip():
    values = [
        "0",
        "1",
        "10",
        "1010",
        "1111",
        "101101",
        "11111111",
        "10000000000",
    ]

    for binary in values:
        assert hex_to_bin(bin_to_hex(binary)) == binary


# =========================
# Hex → Binary → Hex
# =========================

def test_hex_binary_roundtrip():
    values = [
        "0",
        "1",
        "A",
        "F",
        "10",
        "2D",
        "FF",
        "400",
        "FFFF",
    ]

    for hexadecimal in values:
        assert bin_to_hex(hex_to_bin(hexadecimal)) == hexadecimal
