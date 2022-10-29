from bindec import bin_dec

def bin_oct(bin):
    decimal = bin_dec(bin)
    octal = oct(decimal)
    octal = octal.split('o')
    return octal

