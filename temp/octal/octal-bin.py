from octal_dec import oct_dec

def oct_bin(octal):
    decimal = oct_dec(octal)
    binary = bin(decimal)
    Splitted_binary = binary.split('b')[1]
    return Splitted_binary


