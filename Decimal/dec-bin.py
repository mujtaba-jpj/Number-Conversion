def dec_bin(decimal):
    #Initialzing and Assigning Decimal
    binary = bin(decimal)

    #Splitting the string in 2 parts: 0b, 11101000
    binary = binary.split("b")[1]
    return binary

