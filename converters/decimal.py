#==============Decimal To Binary==============
def validate_input(decimal: str) -> int:
    try:
        decimal = int(decimal)
    except ValueError:
         raise ValueError("Invalid dec format")

    return decimal    

# 5 = 5/2 = 2(rem 1) 2/2 = 1(rem 0) 1/2 = 0(rem 1) | 5 = 101(reverse order of rems)
def dec_to_bin(decimal: str) -> str:
    decimal = validate_input(decimal)

    result = ""

    while decimal!=0:
        result = str(decimal%2) + result
        decimal //= 2

    return result

dth = {
    10 : "A",
    11 : "B",
    12 : "C",
    13 : "D",
    14 : "E",
    15 : "F"
}

def dec_to_hex(decimal: str) -> str:
    decimal = validate_input(decimal)

    result = ""

    while decimal != 0 :
        rem = decimal % 16
        if rem >=10:
            result = dth[rem] + result
        else:
            result = str(rem) + result
        decimal //= 16

    return result

