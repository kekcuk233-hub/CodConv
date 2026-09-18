import sys
from converters.binary import bin_to_dec, bin_to_hex
from converters.decimal import dec_to_bin, dec_to_hex

def main() -> None:
    if len(sys.argv) != 3:
        print("Invalid arguments. Write --help for instructions")
        return

    command = sys.argv[1]
    value = sys.argv[2]
    #print(sys.argv[0], command,value)

    try:
        if command == "bin_to_dec":
            print(bin_to_dec(value))

        elif command == "bin_to_hex":
            print(bin_to_hex(value))

        elif command == "dec_to_bin":
            print(dec_to_bin(value))

        elif command == "dec_to_hex":
            print(dec_to_hex(value))
    except ValueError as error:
                print(f"Error: {error}")

if __name__ == "__main__":
    main()
