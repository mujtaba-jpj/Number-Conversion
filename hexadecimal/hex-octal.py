def hex_oct(hex):
    decimal = int(hex,16)
    octal = oct(decimal)
    octal = octal.split("o")[1]
    return octal
