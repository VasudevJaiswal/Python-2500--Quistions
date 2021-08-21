# Basic Variable Assignment

print('''A student learning Python was trying to make a function.
 His code should concatenate a passed string name with string  'Vasudev' and 
 store it in a variable called result. He needs your help to fix this code. ''')

def name_String():
    a = input("Enter First String : ")
    b = input("Enter Seconed String : ")
    result = str(a) + str(b)
    print(result)
    return result


name_String()

# Program  not closed emmidately 

input("Please Click to Enter to End the Program ")