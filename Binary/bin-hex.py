from bindec import bin_dec

def bin_hex(bin):
    decimal = bin_dec(bin)
    hexadecimal = hex(decimal)  
    hexadecimal = hexadecimal.split('x')
    print(hexadecimal[1])
    return hexadecimal

