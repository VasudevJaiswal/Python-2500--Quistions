# There is a single operator in Python, capable of providing the remainder of a division operation. 
# Two numbers are passed as parameters. 
# The first parameter divided by the second parameter will have a remainder, possibly zero. Return that value.


dividend = int(input("Enter the  Divident Number : "))
divisor = int(input("Enter the Divisor Number : "))

# Find the division of the operation 
division = dividend/divisor
print("\nDivison of the Operation is - ",str(division))

# Find the quotient of the operation 
quotient = dividend//divisor
print("\nQuotient of the Operation is - ",str(quotient))


# Find the remainder of the operation 
remainder = dividend%divisor
print("\nRemainder of the Operation is - ",str(remainder))


# Program  not closed emmidately 

input("\nPlease Click to Enter to End the Program ")