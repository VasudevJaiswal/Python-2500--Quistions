# Football Points

print('''Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.

wins get 3 points
draws get 1 point
losses get 0 point''')

def Points(wins_get,draws_get,losses_get):
    
    wins = int(input("Enter wins number : "))
    wins_get = wins*3
    # print(wins_get) 

    draws = int(input("Enter draws number : "))
    draws_get = draws*1
    # print(draws_get)

    losses = int(input("Enter the losses number : "))
    losses_get = losses*0
    # print(losses_get)

    total = wins_get+draws_get+losses_get
    print(total)


Points()