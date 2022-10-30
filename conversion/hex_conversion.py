def hex_bin(hex):
    decimal = int(hex,16)
    binary = bin(decimal)
    binary = binary.split("b")[1]
    return binary

def hex_dec(hex):

    decimal = int(hex, 16) #Hex = Hex, 16= Hex base
    return decimal

def hex_oct(hex):
    decimal = int(hex,16)
    octal = oct(decimal)
    octal = octal.split("o")[1]
    return octal
