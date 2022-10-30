
def bin_dec(binary):
    #Asking for Binary Input
    binary = str(binary)
    decimal = 0

    #Converting Bin to Dec
    for digit in binary:
        decimal = decimal*2 + int(digit)

    #Printing Dec
    return decimal

def bin_oct(bin):
    decimal = bin_dec(bin)
    octal = oct(decimal)
    octal = octal.split('o')[1]
    return octal

def bin_hex(bin):
    decimal = bin_dec(bin)
    hexadecimal = hex(decimal)  
    hexadecimal = hexadecimal.split('x')[1]
    return hexadecimal

