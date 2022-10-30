def dec_bin(decimal):
    #Initialzing and Assigning Decimal
    binary = bin(decimal)

    #Splitting the string in 2 parts: 0b, 11101000
    binary = binary.split("b")[1]
    return binary

    
def dec_hex(decimal):
    hexadecimal = hex(decimal)
    hexadecimal = hexadecimal.split("x")[1]
    return hexadecimal

def dec_oct(dec):
    octal = oct(dec)
    octal = octal.split("o")[1]
    return octal

