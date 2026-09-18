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

bth = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9", 
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F"
}

def bin_to_hex(binary: str) -> str:
    validate_input(binary)

    while len(binary)%4 != 0 :
         binary = "0" + binary

    result = ""
    for i in range(0, len(binary), 4):
        nibble = binary[i:i+4]
        result += bth[nibble] 

    return result

