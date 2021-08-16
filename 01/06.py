# Create a function that finds the maximum range of a triangle's third edge, 
# where the side lengths are all integers.

print("reate a function that finds the maximum range of a triangle's third edge")

def max_tri():
    side1 = int(input("Enter the integer - side1 : "))
    side2 = int(input("Enter the integer - side2 : "))
    maximum_triangle = (side1+side2)-1
    print("Maximum range of a Triangle's third edge is - ",maximum_triangle)
    return maximum_triangle


max_tri()

# # Program  not closed emmidately 
input("Please Click to Enter to End the Program ")
