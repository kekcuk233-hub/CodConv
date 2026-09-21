from constants import BIN_TO_HEX, NOT_TABLE
from converters.decimal import dec_to_bin

#==============Convertations==============
def validate_input(binary: str) -> None:
    if not binary:
            raise ValueError("Input cannot be empty")
    
    if not all(bit in "01" for bit in binary):
        raise ValueError("Invalid binary number")

#101 = 1*2^2 + 0 *2^1 + 1*2^0 = 5
#my function for learning
def bin_to_dec(binary: str) -> int:
    validate_input(binary)

    result = 0

    for bit in binary:
        result = result*2+int(bit)
    return result

#reference function
# def bin2dec(binary: str) -> int:
#     return int(binary, 2)

def bin_to_hex(binary: str) -> str:
    validate_input(binary)

    while len(binary)%4 != 0 :
         binary = "0" + binary

    result = ""
    for i in range(0, len(binary), 4):
        nibble = binary[i:i+4]
        result += BIN_TO_HEX[nibble] 

    return result

# =========================
# Bitwise Operations
# =========================

def AND(bin1:str, bin2:str) -> str:
    validate_input(bin1)
    validate_input(bin2)

    # result = bin_to_dec(bin1) & bin_to_dec(bin2)
    # print(f"Reference: {dec_to_bin(result)}")
    # print("My realization: ", end= "")

    result2 = ""

    if len(bin1) > len(bin2):
        bin1, bin2 = bin2, bin1

    size_dif = len(bin2) - len(bin1)
    

    for i in range(len(bin1)):
        if bin1[i] == "1" and bin2[i+size_dif] == "1":
            result2 += "1"
        else:
            result2 += "0"

    return result2.lstrip("0") or "0"

def OR(bin1: str, bin2: str) -> str:
    validate_input(bin1)
    validate_input(bin2)

    print(f"Reference Result: {dec_to_bin(bin_to_dec(bin1) | bin_to_dec(bin2))}")
    
    result = ""
    
    if len(bin1) < len(bin2):
        bin1, bin2 = bin2, bin1
    
    # size_dif = len(bin1) - len(bin2)

    # while size_dif != 0:
    #     bin2 = "0" + bin2
    #     size_dif -= 1

    bin2 = bin2.zfill(len(bin1))
    
    for i in range(len(bin1)):
        if bin1[i] == "0" and bin2[i] == "0":
            result += "0"
        else:
            result += "1"
    
    return result.lstrip("0") or "0"

def NOT(binary: str) -> str:
    validate_input(binary)

    result = ""

    for bit in binary:
        result += NOT_TABLE[bit]

    return result
