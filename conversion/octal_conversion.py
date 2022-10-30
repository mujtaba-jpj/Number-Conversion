def oct_dec(octal):
    decimal = 0

    l = len(octal)
    for x in octal:
        l = l-1    
        decimal += pow(8,l) * int(x)    
    return decimal


def oct_bin(octal):
    decimal = oct_dec(octal)
    binary = bin(decimal)
    Splitted_binary = binary.split('b')[1]
    return Splitted_binary


def oct_hex(octal):
    decimal = oct_dec(octal)
    hexadecimal = hex(decimal)
    hexadecimal = hexadecimal.split('x')[1]
    return hexadecimal
