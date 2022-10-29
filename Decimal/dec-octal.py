#Initialzing and Assigning Octal
Octal = (oct(int(input("Input a Decimal Number: "))))

#Splitting the String
FixedOctal = Octal.split("0o")

#Displaying the Resulting Octal number
print(FixedOctal[1])