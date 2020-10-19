def bin_to_oct(binary):
    decimal = int(binary, 2)
    return oct(decimal)

def oct_to_bin(octal):
    decimal = int(octal, 8)
    return bin(decimal)


if __name__ == "__main__":
    print(bin_to_oct("111"))
    print(oct_to_bin("7"))