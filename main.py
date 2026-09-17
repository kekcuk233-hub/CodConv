#==============Binary To Decimal==============
def validate_input(binary: str) -> bool:
    if binary == "":
        print("input cant be empty")
        return False
    
    if all(bit in "01" for bit in binary):
        return True
    else:
        return False

#101 = 1*2^2 + 0 *2^1 + 1*2^0 = 5
#my function for learning
def binary_to_dec(binary: str) -> int:
    result = 0

    for bit in binary:
        result = result*2+int(bit)
    return result

#reference function
# def bin2dec(binary: str) -> int:
#     return int(binary, 2)

#==============Decimal To Binary==============
# 5 = 5/2 = 2(rem 1) 2/2 = 1(rem 0) 1/2 = 0(rem 1) | 5 = 101(reverse order of rems)
def decimal_to_binary(decimal: int) -> str:
    result = ""

    while decimal!=0:
        result = str(decimal%2) + result
        decimal //= 2
    return result

def main() -> None:
    binary = input("Write binary number: ")
    print(binary)
    if validate_input(binary): 
        dec1 = binary_to_dec(binary)
        #dec2 = bin2dec(binary)
        print(f"Decimal: {dec1}")
    else: 
        print("Invalid binary number")
        
    #-------------------------------------------
    
    decimal = input("Write decimal number: ")
    try: 
        decimal = int(decimal)
    except ValueError:
        print("Wrong decimal format")
    else:
        bin = decimal_to_binary(decimal)
        print(f"Binary: {bin}")

if __name__ == "__main__":
    main()
