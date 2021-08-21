# The Farm Problem

print('''In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:

chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.

Examples ''')

def legs_count():
    chick = int(input("Enter Number of Chickens : "))
    chick_tot = chick*2

    cows = int(input("Enter Number of Cows : "))
    cows_tot = cows*4

    pigs = int(input("Enter Number of Pigs : "))
    pigs_tot = pigs*4

    # Total of Animals legs 

    total = chick_tot+cows_tot+pigs_tot
    print("Total No. of All animals legs :  ",str(total))
    return total



legs_count()

# Program  not closed emmidately 

input("Please Click to Enter to End the Program ")