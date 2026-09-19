from constants import HEX_TO_BIN, HEX_TO_DEC

def validate_input(hex: str) -> bool:
    if not all(h in "0123456789ABCDEF" for h in hex):
        raise ValueError("Invalid hex input")

    return True

def hex_to_bin(hex: str) -> str:
    validate_input(hex)

    result = ""

    for h in hex:
        result += HEX_TO_BIN[h]

    return result

def hex_to_dec(hex: str) ->int:
    validate_input(hex)

    result = 0

    for h in hex:
        if h in HEX_TO_DEC:
            result = result * 16 + HEX_TO_DEC[h]
        else:
            result = result * 16 + int(h) 

    return result
