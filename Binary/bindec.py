def bin_dec(binary):
    #Asking for Binary Input
    binary = str(binary)
    decimal = 0

    #Converting Bin to Dec
    for digit in binary:
        decimal = decimal*2 + int(digit)

    #Printing Dec
    return decimal


