from octal_dec import oct_dec

def oct_hex(octal):
    decimal = oct_dec(octal)
    hexadecimal = hex(decimal)
    hexadecimal = hexadecimal.split('x')[1]
    return hexadecimal
