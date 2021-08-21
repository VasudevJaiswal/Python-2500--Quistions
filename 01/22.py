# String to Integer and Vice Versa

print('''Write two functions:

to_int() : A function to convert a string to an integer.
to_str() : A function to convert an integer to a string. ''')



print("1. to_int() : A function to convert a string to an integer.")
def to_int():
    string  = input("Enter Any string : ")
    string_to_int = int(string)
    print(string_to_int)

to_int()

print("2.A function to convert an integer to a string. ")
def to_str():
    integer = int(input("Enter any integes : "))
    int_to_string = str(integer)
    print(int_to_string)


to_str()