import argparse
from converters.binary import bin_to_dec, bin_to_hex, AND, OR, NOT
from converters.decimal import dec_to_bin, dec_to_hex
from converters.hex import hex_to_bin, hex_to_dec

def main() -> None:
    parser = argparse.ArgumentParser(prog="SecTools", description="Program with usefull cybersec tools")

    # parser.add_argument("--list", action="store_true", help="Показать все доступные функции")

    # sub = parser.add_subparsers(dest="command")

    parser.add_argument('functionName')
    parser.add_argument('value1')
    parser.add_argument('value2', nargs="?")

    args = parser.parse_args()

    command = args.functionName.lower()
    value1 = args.value1

    try:
        if command == "bin_to_dec":
            print(bin_to_dec(value1))
        elif command == "bin_to_hex":
            print(bin_to_hex(value1))

        elif command == "dec_to_bin":
            print(dec_to_bin(value1))
        elif command == "dec_to_hex":
            print(dec_to_hex(value1))

        elif command == "hex_to_bin":
            print(hex_to_bin(value1))
        elif command == "hex_to_dec":
            print(hex_to_dec(value1))

        elif command == "and":
            value2 = args.value2
            if value2 == None:
                raise ValueError("AND takes 2 arguments")
            print(AND(value1, value2))
        elif command == "or":
            value2 = args.value2
            if value2 == None:
                raise ValueError("OR takes 2 arguments")
            print(OR(value1, value2))
        elif command == "not":
             print(NOT(value1))

        else: 
             raise ValueError(f"Unknown command: {command}")
    except ValueError as error:
                print(f"Error: {error}")

if __name__ == "__main__":
    main()
