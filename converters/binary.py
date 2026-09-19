from constants import BIN_TO_HEX

#==============Binary To Decimal==============
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

