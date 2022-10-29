def hex_bin(hex):
    decimal = int(hex,16)
    binary = bin(decimal)
    binary = binary.split("b")[1]
    return binary
