def oct_dec(octal):
    decimal = 0

    l = len(octal)
    for x in octal:
        l = l-1    
        decimal += pow(8,l) * int(x)    
    return decimal

