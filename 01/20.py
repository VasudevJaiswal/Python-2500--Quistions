# Convert Hours and Minutes into Seconds

print("Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.")

def time(): # or def time(hours,minutes):
    hour = int(input("Enter the Hours : "))
    min = int(input("Enter the Minutes : "))
    result = (hour)*3600+(min)*60
    print("Converted Successfully into Seconeds : ",str(result))
    return result

time()  # or time(hour,min)

# Program  not closed emmidately 

input("Please Click to Enter to End the Program ")