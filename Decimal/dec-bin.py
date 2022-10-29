#Initialzing and Assigning Decimal
Decimal = bin(int(input("enter a num: ")))

#Splitting the string in 2 parts: 0b, 11101000
FixedDecimal = Decimal.split("0b")

#Print the 1 part of string i.e 111010000 and ignore the 0 port i.e 0b
print(Decimal[1])