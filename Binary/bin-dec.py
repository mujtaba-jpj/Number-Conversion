#Asking for Binary Input
binary = input('enter a number: ')
decimal = 0

#Converting Bin to Dec
for digit in binary:
    decimal = decimal*2 + int(digit)

#Printing Dec
print(decimal)