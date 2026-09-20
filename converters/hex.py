from constants import HEX_TO_BIN, HEX_TO_DEC

def validate_input(value: str) -> bool:
    if not value:
        raise ValueError("Input cant be empty")
    
    if not all(h in "0123456789ABCDEF" for h in value):
        raise ValueError("Invalid hex input")

    return True

def hex_to_bin(value: str) -> str:
    value = value.upper()
    validate_input(value)

    result = ""

    for h in value:
        result += HEX_TO_BIN[h]

    result = result.lstrip("0")

    return result or "0"

def hex_to_dec(value: str) ->int:
    value = value.upper()
    validate_input(value)

    result = 0

    for h in value:
        if h in HEX_TO_DEC:
            result = result * 16 + HEX_TO_DEC[h]
        else:
            result = result * 16 + int(h) 

    return result
