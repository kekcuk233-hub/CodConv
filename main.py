import sys
import argparse
from converters.binary import bin_to_dec, bin_to_hex
from converters.decimal import dec_to_bin, dec_to_hex
from converters.hex import hex_to_bin, hex_to_dec

def main() -> None:
    parser = argparse.ArgumentParser(prog="SecTools", description="Program with usefull cybersec tools")

    parser.add_argument('functionName')
    parser.add_argument('value')

    args = parser.parse_args()
    print(args.functionName, args.value)

    # command = sys.argv[1]

    # if command == "--help":
    #     with open("helpInstr.md") as f:
    #         print(f.read())
    #     return

    # if len(sys.argv) != 3:
    #     print("Invalid arguments. Write --help for instructions")
    #     return

    # value = sys.argv[2]
    # #print(sys.argv[0], command,value)

    # try:
    #     if command == "bin_to_dec":
    #         print(bin_to_dec(value))
    #     elif command == "bin_to_hex":
    #         print(bin_to_hex(value))

    #     elif command == "dec_to_bin":
    #         print(dec_to_bin(value))
    #     elif command == "dec_to_hex":
    #         print(dec_to_hex(value))

    #     elif command == "hex_to_bin":
    #         print(hex_to_bin(value))
    #     elif command == "hex_to_dec":
    #         print(hex_to_dec(value))

    # except ValueError as error:
    #             print(f"Error: {error}")

if __name__ == "__main__":
    main()
